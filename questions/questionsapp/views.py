import requests
import re
from lxml import etree
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.db.models import Count

from questionsapp.models import User, Question

# Create your views here.
def index(request, user=None):
    users_count = User.objects.count()
    questions_count = Question.objects.count()
    top10 = Question.objects.annotate(num_users=Count('users')).order_by('-num_users')[:10]
    if user is not None:
        user = User.objects.get(pk=user)
    context = dict(users_count=users_count, questions_count=questions_count, top10=top10, user=user)
    return render(request, 'questionsapp/index.html', context)

def extract_username(url):
    return re.findall('profile/([^/]*)', url)[0]

def add_user(request):
    parser = etree.HTMLParser()
    url = request.POST['user']
    username = extract_username(url)
    url = 'http://www.okcupid.com/profile/%s/questions?she_care=1' % users_count
    html = requests.get(url).text
    #html = file('q.htm').read()
    parser.feed(html)
    dom = parser.close()
    questions_div = dom.find('body/div[@id="body_wrapper"]/div[@id="wrapper"]/div[@id="page"]/div[@id="main_content"]/div[@class="monolith"]/div[@class="big_dig clearfix "]')
    try:
        user = User.objects.get(name=username)
    except User.DoesNotExist:
        user = User(url=url, name=username)
        user.save()
    for i in questions_div.getiterator():
        if str(i.get('id')).startswith('qtext_'):
            q_id = i.get('id').split('_')[1]
            try:
                q_obj = Question.objects.get(pk=q_id)
            except Question.DoesNotExist:
                q_text = i.find('p').text
                q_obj = Question(id=q_id, text=q_text)
                q_obj.save()
            user.question_set.add(q_obj)

    user.save()
    return HttpResponseRedirect(reverse('success', args=[user.id]))


def details(request, questions=None):
    return HttpResponse(questions)
