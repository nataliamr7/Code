"""items URL Configuration
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<name>', views.item, name='item')
]
