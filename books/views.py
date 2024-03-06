from django.http import JsonResponse
from django.shortcuts import render
from .models import PDFPage
from .utils import translation


def page_detail(request, page_number):
    page = PDFPage.objects.get(page_number=page_number)
    return render(request, 'bool/page.html', {'page': page})


def word_transl(request, source_text):
    transl = translation(source_text)  # Предположим, что функция init_transl возвращает перевод текста
    print(transl)
    return JsonResponse({"translation": transl})
