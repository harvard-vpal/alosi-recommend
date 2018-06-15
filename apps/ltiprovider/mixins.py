import logging

from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt
from lti import InvalidLTIRequestError
from lti.contrib.django import DjangoToolProvider
from oauthlib import oauth1

from apps.ltiprovider.validator import SignatureValidator
from apps.ltiprovider.models import LtiUser, LtiConsumer


log = logging.getLogger(__name__)


class LtiLaunchMixin(object):
    """
    Mixin for LTI launch views
    Workflow:
    - LTI authentication
        - look up secret using consumer key
        - request verification
    - Get or create user based on (user_id, tool consumer instance id)
    """

    @csrf_exempt
    @xframe_options_exempt
    def dispatch(self, request, *args, **kwargs):
        validate_lti_request(request)
        get_or_create_lti_user(request)
        request.session['lti_session'] = request.POST['oauth_nonce']
        # put lti user id in session
        request.session['lti_user_id'] = request.POST['user_id']
        return super(LtiLaunchMixin, self).dispatch(request, *args, **kwargs)


class LtiSessionMixin(object):
    """
    Mixin that enforces that user has an LTI session
    LTI session is indicated by the existence of the 'lti_session' session key/value
    """
    @xframe_options_exempt
    def dispatch(self, request, *args, **kwargs):
        lti_session = request.session.get('lti_session')
        if not lti_session:
            log.error('LTI session is not found, Request cannot be processed')
            raise PermissionDenied("Content is available only through LTI protocol.")
        return super(LtiSessionMixin, self).dispatch(request, *args, **kwargs)


def validate_lti_request(request):
    """
    Check if LTI launch request is valid, and raise an exception if request is not valid
    An LTI launch is valid if:
    - The launch contains all the required parameters
    - The launch data is correctly signed using a known client key/secret pair
    :param request:
    :return: none
    """
    try:
        tool_provider = DjangoToolProvider.from_django_request(request=request)
        # validate based on originating protocol if using reverse proxy
        if request.META.get('HTTP_X_FORWARDED_PROTO') == 'https':
            tool_provider.launch_url = tool_provider.launch_url.replace('http:', 'https:', 1)
        validator = SignatureValidator()
        is_valid_lti_request = tool_provider.is_valid_request(validator)
    except (oauth1.OAuth1Error, InvalidLTIRequestError, ValueError) as err:
        is_valid_lti_request = False
        log.error('Error happened while LTI request: {}'.format(err.__str__()))
    if not is_valid_lti_request:
        raise Http404('LTI request is not valid')


def get_or_create_lti_user(request):
    """
    Get or create lti user based on lti launch params:
        'user_id',
        'oauth_consumer_key'
        'tool_consumer_instance_guid'
    Handle some cases where these request parameters are not found or invalid
    :return: (LtiUser model instance, bool)
    """
    # user id
    user_id = request.POST.get('user_id')
    if not user_id:
        raise Exception('User id not in lti launch parameters')

    # consumer key
    lti_consumer = LtiConsumer.objects.get(consumer_key=request.POST.get('oauth_consumer_key'))

    # tool consumer instance guid
    tool_consumer_instance_guid = request.POST.get('tool_consumer_instance_guid')
    if not tool_consumer_instance_guid:
        # tool_consumer_instance_guid = infer_tool_consumer_instance_guid(request)
        tool_consumer_instance_guid = lti_consumer.default_tool_consumer_instance_guid

    # get or create the lti user
    lti_user, created = LtiUser.objects.get_or_create(
        user_id=user_id,
        lti_consumer=lti_consumer,
        tool_consumer_instance_guid=tool_consumer_instance_guid
    )
    return lti_user, created
