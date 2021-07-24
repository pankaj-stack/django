from django.shortcuts import render
from django.http.response import HttpResponse
import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .serializers import Category_modelSerializer,ProductModelSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def inventary_management_system_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer = ProductModelSerializer(data = pythondata) 
        if serializer.is_valid():
            serializer.save()
            response = {'msg':'Data Created'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
