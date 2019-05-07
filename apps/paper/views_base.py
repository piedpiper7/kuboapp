from django.views.generic.base import View
from paper.models import Paper


class PaperListView(View):
    def get(self, request):
        json_list = []
        papers = Paper.objects.all()[:10]
        # for paper in papers:
        #     json_dict = {}
        #     json_dict['name'] = paper.name
        #     json_dict['types'] = paper.types.name
        #     json_dict['level'] = paper.level
        #     json_list.append(json_dict)

        # from django.forms.models import model_to_dict
        # for paper in papers:
        #     json_dict = model_to_dict(paper)
        #     json_list.append(json_dict)

        import json
        from django.core import serializers
        json_data = serializers.serialize('json', papers)
        json_data = json.loads(json_data)
        from django.http import HttpResponse, JsonResponse

        return JsonResponse(json_data, safe=False)



        # import json
        # from django.core import serializers
        # json_data = serializers.serialize('json', papers)
        # json_data = json.loads(json_data)
        # from django.http import HttpResponse, JsonResponse
        # return JsonResponse(json_data, safe=False)

