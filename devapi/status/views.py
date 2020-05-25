import json
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from .mixins import CSRFExemptMixin
from .models import Status
from .forms import StatusModelForm
from .utils import is_json
# Create your views here.

#create, update, delete, retrive(1) /api/status/id/
class StatusDetailAPIView(CSRFExemptMixin, View):
    '''
    Retrive, update, delete
    '''
    def get(self, request, id, *args, **kwargs):
        obj = Status.objects.get(id=id)
        #if no status found
        # if obj in None:
        #     error_data = json.dumps({"message":"no any status found"})
        #     return HttpResponse(error_data, content_type='application/json', status=404)

        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = json.dumps({"message": "Not allowed please use create end point .i.e./api/status/"})
        return HttpResponse(json_data, content_type='application/json' ,status=403)


    def put(self, request, id, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message":"Invalid data"})
            return HttpResponse(error_data, content_type='application/json', status=400)

        obj = get_object_or_404(Status, id=id)
        data = json.loads(obj.serialize())
        passed_data = json.loads(request.body)
        for key, value in passed_data.items():
            data[key] = value
        form = StatusModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return HttpResponse(obj_data, content_type='application/json', status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return HttpResponse(data, content_type='application/json', status=400)

        json_data = json.dumps({"message":"sth"})
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, id, *args, **kwargs):
        obj = get_object_or_404(Status, id=id)

        deleted_ = obj.delete()
        print(deleted_)
        json_data = json.dumps({"message":"Successfully deleted"})
        return HttpResponse(json_data, content_type='application/json', status=200)


#retrive all /api/status/
class StatusListAPIView(CSRFExemptMixin,View):
    '''
    list retrive and create
    '''
    def get(self, request, *args, **kwargs):
        qs  = Status.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message":"Invalid data"})
            return HttpResponse(error_data, content_type='application/json', status=400)
        data = json.loads(request.body)
        form = StatusModelForm(data)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return HttpResponse(obj_data, content_type='application/json', status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return HttpResponse(data, content_type='application/json', status=400)
        data = json.dumps({"message": "unknown"})
        return HttpResponse(data, content_type='application/json', status=400) #400 bad request
        # return HttpResponse(data, content_type='application/json', status=201) #201 if sucess

    def delete(self, request, *args, **kwargs):
        data = json.dumps({"message": "you can't delete an entire list"})
        return HttpResponse(data, content_type='application/json', status=404) #404 forbidden
