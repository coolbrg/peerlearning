from django.urls import path

from . import views  # basically access to views index method

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:question_id>/', views.detail, name='detail'),
]
