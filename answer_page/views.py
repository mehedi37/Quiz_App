from django.shortcuts import render
from quiz.models import quiz

# Create your views here.

ans = quiz.objects.all().values_list('answer', flat=True)


def answer(request, number):
    if request.method == 'POST':
        given_answer = request.POST['answer']
        print("Your answer ", given_answer, number, ans[number - 1])

        return render(request, 'answer.html', {
            'number': number,
            'is_correct': 'correct' if ans[number - 1] == given_answer else 'wrong',
            'given_answer': given_answer,
        }
        )
    else:
        return render(request, 'answer.html', {
            'number': number,
            'is_correct': 'False',
            'given_answer': 'None',
        })
