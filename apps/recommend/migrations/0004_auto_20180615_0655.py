# Generated by Django 2.0.5 on 2018-06-15 06:55

from django.db import migrations
import uuid


def gen_uuid(apps, schema_editor):
    Collection = apps.get_model('recommend', 'Collection')
    for row in Collection.objects.all():
        row.collection_id = uuid.uuid4()
        row.save(update_fields=['collection_id'])
    Choice = apps.get_model('recommend', 'Choice')
    for row in Choice.objects.all():
        row.key = uuid.uuid4()
        row.save(update_fields=['key'])


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0003_auto_20180615_0653'),
    ]

    operations = [migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop), ]