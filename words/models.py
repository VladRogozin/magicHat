from django.db import models


def audio_file_name(instance):
    new_filename = f"{instance.origin_word}.jpg"
    return f'words_image/{new_filename}'


class Word(models.Model):
    origin_word = models.CharField(max_length=100, default=None)
    rus_translation = models.CharField(max_length=255, default=None)
    image = models.FileField(upload_to=audio_file_name, default=None, blank=True, null=True)
    support_word = models.JSONField(default=dict, blank=True, null=True)
    explanations = models.TextField(default='', blank=True, null=True,)