import json
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.core import serializers

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from operation.models import UserLike
from .models import Type, Paper, Topic, Answer
from .forms import UserAnswerForm


class TypeView(View):

    def get(self, request):
        all_type = Type.objects.all()
        # type_f = Type.objects.filter(is_parents=True).all()
        # type_s = Type.objects.filter(is_parents=False).all()

        search_keywords = request.GET.get("keywords", "")
        if search_keywords:
            all_type = all_type.filter(Q(name__icontains=search_keywords)|Q(instr__contains=search_keywords))

        return render(request, "type-list.html", {
            "all_type": all_type,
        })


# @csrf_exempt
# def post(request):
#     type_id = request.POST.get('paper_type')
#     all_papers = Paper.objects.all()
#     return render(request, 'type_paper.html', {
#         "type_id": type_id,
#         "all_papers": all_papers
#     })


class TypePaperView(View):

    def get(self, request, type_id):
        types = Type.objects.get(id=int(type_id))
        all_types = Type.objects.all()
        all_papers = Paper.objects.all()
        # all_papers = types.paper_set.all()
        return render(request, 'type_paper.html', {
            "all_types": all_types,
            # "parents_id": parents_id,
            "types": types,
            "all_papers": all_papers,
        })


class PaperView(View):

    def get(self, request, paper_id):
        types = Type.objects.get(id=int(paper_id))
        all_papers = types.paper_set.all()
        search_keywords = request.GET.get("keywords", "")
        if search_keywords:
            all_papers = all_papers.filter(Q(name__icontains=search_keywords))
        return render(request, 'paper-list.html', {
            "types": types,
            "all_papers": all_papers
        })


# class AddFavView(View):
#
#     def post(self, request):
#


class TopicListView(View):

    def get(self, request, topic_id):
        papers = Paper.objects.get(id=int(topic_id))
        all_topics = papers.topic_set.all()
        all_answer = Answer.objects.all()

        # try:
        #     page = request.GET.get('page', 1)
        # except PageNotAnInteger:
        #     page = 1
        #
        # p = Paginator(all_topics, 1, request=request)
        #
        # topic = p.page(page)
        return render(request, 'topic-list.html', {
            "all_topics": all_topics,
            "all_answer": all_answer
        })


class FinalAnswerView(View):

    def get(self, request):
        all_result = Topic.objects.filter(papers_id=1).values("id")
        return render(request, 'result.html', {
            "all_result": all_result
        })


def page(request):
    data = request.GET
    num = data.get('num')
    result = serializers.serialize("json", Topic.objects.filter(papers_id=num))
    return HttpResponse(result, content_type='application/json')

