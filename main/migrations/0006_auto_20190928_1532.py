# Generated by Django 2.1.2 on 2019-09-28 19:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_event_last_edit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='last_edit',
        ),
        migrations.AlterField(
            model_name='event',
            name='volunteers',
            field=models.ManyToManyField(related_name='volunteers_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
