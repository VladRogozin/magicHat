# Generated by Django 5.0.2 on 2024-03-01 08:52

import l_historys.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('image', models.FileField(blank=True, default=None, null=True, upload_to=l_historys.models.audio_file_name)),
                ('noun', models.JSONField()),
                ('verbs', models.JSONField()),
                ('prepositions', models.JSONField()),
                ('text', models.TextField()),
            ],
        ),
    ]