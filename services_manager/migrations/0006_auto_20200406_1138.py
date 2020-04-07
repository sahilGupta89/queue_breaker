# Generated by Django 3.0.4 on 2020-04-06 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20200403_0628'),
        ('services_manager', '0005_providerstimeslot_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providerstimeslot',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='providertimeslots', to='users.User'),
        ),
    ]