from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('score', views.score, name='score'),
    path('special', views.special, name='special'),
    path('score_special', views.score_special, name='score_special'),
]