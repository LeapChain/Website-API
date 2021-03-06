# Generated by Django 3.1.1 on 2021-08-19 16:12

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrustedBank',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ip_address', models.GenericIPAddressField()),
                ('port', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(65535)])),
                ('protocol', models.CharField(choices=[('http', 'http'), ('https', 'https')], max_length=5)),
            ],
            options={
                'verbose_name_plural': 'trusted banks',
            },
        ),
        migrations.AddConstraint(
            model_name='trustedbank',
            constraint=models.UniqueConstraint(fields=('ip_address', 'port', 'protocol'), name='trusted_banks_trustedbank_unique_ip_port_proto'),
        ),
    ]
