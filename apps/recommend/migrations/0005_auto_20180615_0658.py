# Generated by Django 2.0.5 on 2018-06-15 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0004_auto_20180615_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='key',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='collection_id',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
