# Generated by Django 5.0.2 on 2024-03-03 12:48

import l_historys.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('l_historys', '0002_history_text_translation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='history',
            name='image2',
            field=models.FileField(blank=True, default=None, null=True, upload_to=l_historys.models.audio_file_name),
        ),
        migrations.AddField(
            model_name='history',
            name='image3',
            field=models.FileField(blank=True, default=None, null=True, upload_to=l_historys.models.audio_file_name),
        ),
        migrations.AddField(
            model_name='history',
            name='image4',
            field=models.FileField(blank=True, default=None, null=True, upload_to=l_historys.models.audio_file_name),
        ),
    ]
