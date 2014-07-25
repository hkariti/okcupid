from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count

from questionsapp.models import User, Question

# Create your views here.
def index(request):
    users_count = User.objects.count()
    questions_count = Question.objects.count()
    top10 = Question.objects.annotate(num_users=Count('users')).order_by('-num_users')[:10]
    context = dict(users_count=users_count, questions_count=questions_count, top10=top10)
    return render(request, 'questionsapp/index.html', context)
