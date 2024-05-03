from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:number>/', views.answer, name='answer'),
]
