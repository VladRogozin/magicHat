from django.shortcuts import render
from .models import History
import random
from django.core.serializers import serialize
from django.http import JsonResponse


def random_history(request, id_story=None):
    histories = History.objects.all()
    if id_story:
        # Если передан id_story, ищем соответствующую историю по id
        try:
            random_history = History.objects.get(id=id_story)
        except History.DoesNotExist:
            # Если история не найдена, возвращаем страницу с ошибкой
            return render(request, 'error.html', {'message': 'История не найдена'})
    else:
        # Если id_story не передан, выбираем случайную историю
        random_history = random.choice(histories)
    # Передаем выбранную историю в шаблон
    return render(request, 'l_historys/random_history.html', {'random_history': random_history, 'histories': histories})



