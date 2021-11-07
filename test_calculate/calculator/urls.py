from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('submitquery', submitquery, name='submitquery'),
]
