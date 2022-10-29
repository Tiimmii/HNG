from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from .models import Point
from .serializers import PointSerializer

# Create your views here.
@csrf_exempt
def point_list(request):
  header = {"Access-Control-Allow-Origin":"*"}
  data = {
    "slackUsername":"Timmi",
    "backend":True,
    "age":18,
    "bio":"I'm oluwole daniel a passionate backend deveolper",
    
  }
  return JsonResponse(data, safe=False, headers=header)


