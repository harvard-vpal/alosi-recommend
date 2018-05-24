# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from apps.ltiprovider.models import LtiConsumer, LtiUser


admin.site.register(LtiConsumer)
admin.site.register(LtiUser)
