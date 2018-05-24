# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from apps.recommend.models import Collection, Choice


admin.site.register(Collection)
admin.site.register(Choice)
