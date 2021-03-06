# Generated by Django 3.1.1 on 2021-10-07 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openings', '0003_auto_20201222_0317'),
    ]

    operations = [
        migrations.AddField(
            model_name='opening',
            name='application_form',
            field=models.CharField(default='-', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='opening',
            name='category',
            field=models.CharField(default='-', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='opening',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
