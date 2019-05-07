import sys
import os


pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+'../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kubo.settings")


import django
django.setup()

from paper.models import Type
from db_tools.data.type_data import row_data


for lv1_type in row_data:
    lv1_ins = Type()
    lv1_ins.name = lv1_type['name']
    lv1_ins.code = lv1_type['code']
    lv1_ins.type_s = 1
    lv1_ins.save()

    for lv2_type in lv1_type['sub_types']:
        lv2_ins = Type()
        lv2_ins.name = lv2_type['name']
        lv2_ins.code = lv2_type['code']
        lv2_ins.type_s = 2
        lv2_ins.parents = lv1_ins
        lv2_ins.save()
