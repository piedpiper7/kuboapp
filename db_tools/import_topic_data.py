import sys
import os


pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+'../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kubo.settings")


import django
django.setup()

from paper.models import Paper, Topic
from db_tools.data.topic_data import row_data

for topic_s in row_data:
    topics = Topic()
    topics.name = topic_s['name']
    topics.answer = topic_s['answer']
    topics.papers_id = topic_s['papers_id']
    topics.num = topic_s['num']
    topics_name = topic_s['types'][-1]
    types = Paper.objects.filter(name=topics_name)
    if types:
        topics.papers = types[0]
    topics.save()
