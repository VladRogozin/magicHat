import json
from django.http import JsonResponse
from django.shortcuts import render
from .utils import request_fo_g4


def index(request):
    return render(request, 'learnAboutWord/play_list.html',)


def check_function(request, type):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        user_message = body_data.get('user_message')

        if type == 'usageInContext':
            result = usage_in_context(user_message)
        elif type == 'toPronounceWord':
            result = to_pronounce_word(user_message)
        elif type == 'articleAndPlural':
            result = article_and_Plural(user_message)
        elif type == 'meaningOfWord':
            result = meaning_of_word(user_message)
        elif type == 'howToMemorize':
            result = how_to_memorize(user_message)
        elif type == 'historyOfWord':
            result = history_of_word(user_message)
        else:
            return JsonResponse({'error': 'Invalid request method'})

        response_data = {
            'user_message': result,
        }
        return JsonResponse(response_data)

    return JsonResponse({'error': 'Invalid request method'})


def usage_in_context(message):
    form_message = f"Как используется слово: '{message}', в контексте в немецком языке. Ответ на русском"
    return request_fo_g4(form_message)


def to_pronounce_word(message):
    form_message = f"Если слово глагол, просклоняй слово как немецком языке: '{message}'. Ответ на русском"
    return request_fo_g4(form_message)


def article_and_Plural(message):
    form_message = f"Какой правильный артикль и множественная форма слова : '{message}' в немецком языке. Ответ на русском"
    return request_fo_g4(form_message)


def meaning_of_word(message):
    form_message = f"Что значит и как его перевести это слово: '{message}' в немецком языке. Ответ на русском"
    return request_fo_g4(form_message)


def how_to_memorize(message):
    form_message = f"Как запомнить это немецкое слово: '{message}'. Ответ на русском"
    return request_fo_g4(form_message)


def history_of_word(message):
    form_message = f"История происхождения слова: '{message}' в немецком языке. Ответ на русском"
    return request_fo_g4(form_message)