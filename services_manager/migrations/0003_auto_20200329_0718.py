# Generated by Django 3.0.4 on 2020-03-29 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services_manager', '0002_categories_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='catagories/'),
        ),
    ]
