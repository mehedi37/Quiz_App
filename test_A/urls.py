from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('quiz.urls')),
    path('answer-page/', include('answer_page.urls')),
    path('', views.home, name='home'),
]
