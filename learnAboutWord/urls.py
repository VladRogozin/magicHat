from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('word/', what_is_meaning, name='what_is_meaning'),
]