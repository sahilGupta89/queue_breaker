# Generated by Django 3.0.4 on 2020-04-13 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services_manager', '0011_consumertimeslotmapping_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumertimeslotmapping',
            name='updated',
        ),
    ]
