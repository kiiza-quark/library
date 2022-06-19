from importlib.resources import path
from . import views
from django.urls import path

urlpatterns = [
    path('', views.studentHome, name='studentHome'),
]
