# Generated by Django 3.0.4 on 2020-03-26 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.TextField(blank=True, max_length=10, unique=True),
        ),
    ]
