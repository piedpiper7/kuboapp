import sys
import os


pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+'../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kubo.settings")


import django
django.setup()

from paper.models import Paper, Type
from db_tools.data.paper_data import row_data

for paper_s in row_data:
    papers = Paper()
    papers.name = paper_s['name']
    papers.level = paper_s['level']
    papers.num = paper_s['num']

    type_name = paper_s['types'][-1]
    types = Type.objects.filter(name=type_name)
    if types:
        papers.types = types[0]
    papers.save()