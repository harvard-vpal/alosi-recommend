# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import DetailView
from apps.ltiprovider.mixins import LtiLaunchMixin
from .models import Collection


class Recommend(LtiLaunchMixin, DetailView):
    """
    Display choices in a collection
    """

    template_name = 'recommend/recommend.html'
    model = Collection

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class RecommendTest(DetailView):
    """
    Version of Recommend View class without LTI auth (for testing)
    """
    template_name = 'recommend/recommend.html'
    model = Collection

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # make api call here
        # placeholder
        recommendation = 'kc1'
        context['recommended_choice'] = recommendation
        return context
