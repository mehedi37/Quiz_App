from django.shortcuts import render
from quiz.models import quiz

# Create your views here.

questions = quiz.objects.all().values_list('question', flat=True)


def quiz(request, number):
    return render(request, 'quiz.html', {
        'number': number,
        'question': questions[number - 1],
    })
