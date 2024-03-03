from django.db import models


def audio_file_name(instance, filename):
    new_filename = f"{instance.name}"
    if instance.image1.name == filename:
        number = 1
    elif instance.image2.name == filename:
        number = 2
    elif instance.image3.name == filename:
        number = 3
    elif instance.image4.name == filename:
        number = 4
    else:
        # Handle this case accordingly, maybe raise an error
        pass

    return f'storys_image/{new_filename}_{number}.jpg'

class History(models.Model):
    name = models.CharField(max_length=100, default='')
    image1 = models.FileField(upload_to=audio_file_name, default=None, blank=True, null=True)
    image2 = models.FileField(upload_to=audio_file_name, default=None, blank=True, null=True)
    image3 = models.FileField(upload_to=audio_file_name, default=None, blank=True, null=True)
    image4 = models.FileField(upload_to=audio_file_name, default=None, blank=True, null=True)
    noun = models.JSONField()
    verbs = models.JSONField()
    prepositions = models.JSONField()
    text = models.TextField()
    text_translation = models.JSONField()


    def __str__(self):
        return "German Language Data"