import random
from django.shortcuts import render
from .models import Word


def random_word(request):
    # Получаем случайное слово из базы данных
    random_word = random.choice(Word.objects.all())
    return render(request, 'words/random_word.html', {'random_word': random_word})