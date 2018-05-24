import hashlib

from django.conf import settings
import shortuuid


def short_token():
    """Generate a 20-character random token"""
    hash = hashlib.sha1(shortuuid.uuid().encode('utf-8'))
    hash.update(settings.SECRET_KEY.encode('utf-8'))
    return hash.hexdigest()[::2]


def infer_tool_consumer_instance_guid(request):
    """
    Use this when tool_consumer_instance_guid is not provided in lti launch
    Could try to detect the request origin domain and use that as the tool_consumer_instance guid
    """
    return NotImplementedError


def is_instructor(request):
    """
    Infer whether user is an instructor-like role based on provided role information
    :param request:
    :return: bool, True if instructor-like, False otherwise
    """
    roles = request.POST.get('roles')
    if roles and set(roles.split(",")).intersection(['Instructor', 'Administrator']):
        return True
    else:
        return False
