from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:number>/', views.quiz, name='quiz'),
]
