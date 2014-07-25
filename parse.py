#!/usr/bin/python
from lxml import etree

parser = etree.HTMLParser()
html = file('q.htm').read()
parser.feed(html)
dom = parser.close()
questions_div = dom.find('body/div[@id="body_wrapper"]/div[@id="wrapper"]/div[@id="page"]/div[@id="main_content"]/div[@class="monolith"]/div[@class="big_dig clearfix "]')
questions = list()
for i in questions_div.getiterator():
    if str(i.get('id')).startswith('qtext_'):
        question = dict()
        question['id'] = i.get('id').split('_')[1]
        question['text'] = i.find('p').text
        questions.append(question)


print questions
