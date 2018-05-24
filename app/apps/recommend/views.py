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
