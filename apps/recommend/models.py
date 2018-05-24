# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import fields


class Collection(models.Model):
    name = fields.CharField(max_length=200)


class Choice(models.Model):
    name = fields.CharField(max_length=200)
    key = fields.CharField(max_length=200)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    image_url = fields.URLField(blank=True, null=True)
