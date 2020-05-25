from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .models import Update
from devapi.mixins import JsonResponseMixin
from django.core.serializers import serialize
# Create your views here.
# def detail_view(request):
#     return render() #return JSON 

def json_example(request):
    data = {
        "count": 1001,
        "content": "some new content"
    }
    return JsonResponse(data)

class JsonCBV(View):
    def get(self, request, *args, **kwagrs):
        data = {
            "count": 100,
            "content": "some new content"
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, requset, *args, **kwagrs):
        data = {
            "count": 1000,
            "content": "from cbv2"
        }
        return self.render_to_json_response(data)


class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = obj.serialize()
        # data = {
        #     "user": obj.user.username,
        #     "content": obj.content
        # }
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        json_data = Update.objects.all().serialize()
        # data = serialize("json", qs, fields=('user', 'content'))
        
        return HttpResponse(json_data, content_type='application/json')
        