from django.contrib import admin
from .models import History

class StoryAdmin(admin.ModelAdmin):
    fields = ('name', 'image1', 'image2', 'image3', 'image4', 'noun', 'verbs', 'prepositions', 'text', 'text_translation')  # Поля, которые будут отображаться и редактироваться

admin.site.register(History, StoryAdmin)
