# Generated by Django 3.0.4 on 2020-04-13 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services_manager', '0009_auto_20200411_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumertimeslotmapping',
            name='updated',
        ),
    ]
