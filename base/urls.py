from django.urls import path
from . import views
urlpatterns = [
    path('', views.indexx, name='index'),
]
