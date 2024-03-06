from django.urls import path
from . import views

urlpatterns = [
    path('books/<int:page_number>/', views.page_detail, name='page_detail'),
    path('translation/<str:source_text>/', views.word_transl, name='word_transl'),
]