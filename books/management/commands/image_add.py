import os
from django.core.management.base import BaseCommand
from words.models import Word


class Command(BaseCommand):
    help = 'Populate image field with image paths for existing words'

    def handle(self, *args, **options):
        words_without_image = Word.objects.filter(image__isnull=True) | Word.objects.filter(
            image='')  # Получаем слова без заполненных explanations

        for word in words_without_image:
            image_path = f'media/media/words_image/{word.origin_word}.jpg'
            print(os.path.exists(image_path))
            if os.path.exists(image_path):
                word.image = image_path
                word.save()
                self.stdout.write(self.style.SUCCESS(f"Image path added for word: {word.origin_word}"))
            else:
                self.stdout.write(self.style.WARNING(f"Image not found for word: {word.origin_word}"))