# Generated by Django 2.1.2 on 2019-09-28 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190928_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='last_edit',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
