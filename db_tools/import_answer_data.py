import sys
import os


pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+'../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kubo.settings")


import django
django.setup()

from paper.models import Topic, Answer
from db_tools.data.answer_data import row_data

for answer_s in row_data:
    answers = Answer()
    answers.content = answer_s['content']
    answers.value = answer_s['value']
    topic_name = answer_s['types'][-1]
    types = Topic.objects.filter(id=topic_name)
    if types:
        answers.topics = types[0]
    answers.save()
