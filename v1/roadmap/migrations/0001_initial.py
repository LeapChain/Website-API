# Generated by Django 3.1.6 on 2021-08-02 18:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0016_auto_20210413_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roadmap',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('task_title', models.CharField(max_length=255)),
                ('estimated_completion_date', models.DateField()),
                ('is_complete', models.BooleanField(default=False)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.coreteam')),
            ],
            options={
                'ordering': ('estimated_completion_date',),
            },
        ),
    ]
