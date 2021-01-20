# Generated by Django 3.1.5 on 2021-01-20 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_site_queue', '0006_sitequeuemanager_queue_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitequeuemanagergroup',
            name='ping_url',
            field=models.CharField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='sitequeuemanagergroup',
            name='ping_url_current',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='sitequeuemanagergroup',
            name='ping_url_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sitequeuemanagergroup',
            name='ping_url_limit',
            field=models.IntegerField(default=5),
        ),
    ]
