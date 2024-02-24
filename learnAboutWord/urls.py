from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('word/<str:type>/', check_function, name='usageInContext'),
]