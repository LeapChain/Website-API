# Generated by Django 3.1.3 on 2020-12-13 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repositories', '0001_initial'),
        ('users', '0004_auto_20201103_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userearnings',
            name='repository',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_earnings', to='repositories.repository'),
        ),
    ]
