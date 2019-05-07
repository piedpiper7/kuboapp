from django.conf.urls import url, include
from .views import TypeView, TypePaperView, PaperView, TopicListView, FinalAnswerView, page

urlpatterns = [
    url(r'^list/$', TypeView.as_view(), name="type_list"),
    # url(r'^click/$', post, name="type_click"),
    url(r'^home/(?P<type_id>\d+)/$', TypePaperView.as_view(), name="type_paper"),
    url(r'^paper/(?P<paper_id>\d+)/$', PaperView.as_view(), name="paper_list"),
    url(r'^topic/(?P<topic_id>\d+)/$', TopicListView.as_view(), name="topic_list"),
    # url(r'^home/(?P<types_id>\d+)/$', TypePaperView.as_view(), name="type_paper"),
    # url(r'^add_fav$', AddFavView.as_view(), name="add_fav")
    # url(r'^result/$', FinalAnswerView.as_view(), name="result"),
    url(r'^result/$', FinalAnswerView.as_view(), name='result'),
    url(r'^page$', page),

 ]