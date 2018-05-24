# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import fields

from apps.ltiprovider.utils import short_token


class LtiConsumer(models.Model):
    """
    Model to manage LTI consumers.

    LMS connections.
    Automatically generates key and secret for consumers.
    """

    consumer_name = models.CharField(max_length=255, unique=True)
    consumer_key = models.CharField(max_length=32, unique=True, default=short_token)  # index
    consumer_secret = models.CharField(max_length=32, unique=True, default=short_token)
    expiration_date = models.DateField(verbose_name='Consumer key expiration date', null=True, blank=True)
    default_tool_consumer_instance_guid = fields.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "LTI Consumer"
        verbose_name_plural = "LTI Consumers"

    def __str__(self):
        return '<LtiConsumer: {}>'.format(self.consumer_name)


class LtiUser(models.Model):
    """
    Model to manage LTI users.
    """

    user_id = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, blank=True, null=True)
    lti_consumer = models.ForeignKey('LtiConsumer', on_delete=models.CASCADE)
    tool_consumer_instance_guid = fields.CharField(max_length=255, default='')

    class Meta(object):
        verbose_name = "LTI User"
        verbose_name_plural = "LTI Users"
        unique_together = (
            ('user_id', 'lti_consumer', 'tool_consumer_instance_guid'),
        )

    def __str__(self):
        return '<LtiUser: {}>'.format(self.user_id)
