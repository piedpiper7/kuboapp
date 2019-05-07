import xadmin
from .models import Type, Paper, Topic, Answer


class TypeAdmin(object):
    list_display = ['name', 'type_s', 'parents', 'add_time']
    list_filter = ['type_s', 'parents', 'add_time']
    search_fields = ['name', ]


class PaperAdmin(object):
    list_display = ['name', 'types', 'level', 'student', 'like', 'add_time']
    list_filter = ['types', 'level', 'add_time']
    search_fields = ['name', ]


class TopicAdmin(object):
    pass


class AnswerAdmin(object):
    pass


xadmin.site.register(Type, TypeAdmin)
xadmin.site.register(Paper, PaperAdmin)
xadmin.site.register(Topic, TopicAdmin)
xadmin.site.register(Answer, AnswerAdmin)