# Generated by Django 3.1.1 on 2021-11-11 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0003_auto_20211004_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='slug',
            field=models.CharField(default='-', max_length=255),
            preserve_default=False,
        ),
    ]
