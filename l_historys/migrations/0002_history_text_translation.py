# Generated by Django 5.0.2 on 2024-03-02 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('l_historys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='text_translation',
            field=models.JSONField(default='none'),
            preserve_default=False,
        ),
    ]
