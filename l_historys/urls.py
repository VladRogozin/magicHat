from django.urls import path
from .views import *

urlpatterns = [

    path('random_history/<int:id_story>/', random_history, name='random_history_with_id'),
    path('random_history/', random_history, name='random_history'),
]