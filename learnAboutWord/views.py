import json
from django.http import JsonResponse
from django.shortcuts import render

from .utils import request_fo_g4


def index(request):
    return render(request, 'learnAboutWord/play_list.html',)


def what_is_meaning(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        user_message = body_data.get('user_message')
        result = request_fo_g4(user_message)
        response_data = {
            'user_message': result,
        }
        return JsonResponse(response_data)

    return JsonResponse({'error': 'Invalid request method'})
