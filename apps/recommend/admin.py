# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from apps.recommend.models import Collection, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 0

class CollectionAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline,
    ]

admin.site.register(Collection, CollectionAdmin)
admin.site.register(Choice)
