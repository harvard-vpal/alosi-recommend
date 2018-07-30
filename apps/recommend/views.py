# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import DetailView
from apps.ltiprovider.mixins import LtiLaunchMixin
from .models import Collection, Choice
from alosi.engine_api import EngineApi
from django.conf import settings
import random


class Recommend(LtiLaunchMixin, DetailView):
    """
    Display choices in a collection
    """

    template_name = 'recommend/recommend.html'
    model = Collection
    slug_url_kwarg = 'collection_id'
    slug_field = 'collection_id'

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_recommend_context_data(self, context, **kwargs)


class RecommendTest(DetailView):
    """
    Version of Recommend View class for testing:
    No LTI auth
    Still makes API call
    """
    template_name = 'recommend/recommend.html'
    model = Collection
    slug_url_kwarg = 'collection_id'
    slug_field = 'collection_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_recommend_context_data(self, context, **kwargs)


class RecommendUITest(DetailView):
    """
    Version of Recommend View class for testing
    No LTI auth
    No API call
    """
    template_name = 'recommend/recommend.html'
    model = Collection
    slug_url_kwarg = 'collection_id'
    slug_field = 'collection_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        collection = context['collection']
        context['recommended_choice'] = random.choice(collection.choice_set.all())
        return context


def get_recommend_context_data(view, context, **kwargs):
    """
    The main functionality (i.e. api call to engine) is out here so that it can go in both the LTI and test view
    :param view: DetailSet view instance
    :param context: initial context from get_context_data
    :param kwargs: kwargs from get_context_data
    :return: modified context to pass to template
    """
    collection = context['collection']

    # make api call to engine
    api = EngineApi(host=settings.ENGINE_URL, token=settings.ENGINE_TOKEN)
    data = dict(
        learner=dict(
            user_id=view.request.session.get('lti_user_id', 'placeholder'),
            tool_consumer_instance_guid=settings.DEFAULT_TOOL_CONSUMER_INSTANCE_GUID
        ),
        collection=collection.collection_id,
        sequence=[],
    )
    r = api.recommend(**data)
    if not r.ok:
        raise Exception('recommendation api call failed: {}'.format(r.text))
    try:
        key = r.json()['source_launch_url']
        choice = Choice.objects.get(key=key)
    except Choice.DoesNotExist:
        raise Exception("Could not find Choice with key={}".format(key))
    # add recommended choice to context data
    context['recommended_choice'] = choice
    return context
