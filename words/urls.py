from django.urls import path
from .views import *

urlpatterns = [
    path('random/', random_word, name='random_word'),
]