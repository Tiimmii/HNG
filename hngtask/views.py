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
  point = Point.objects.all()
  if point.count()<1:
    Point.objects.create(slackUsername='Timmi', backend=True, age=18, bio="I'm Oluwole Daniel an undergraduate currently studying Bsc computer science and a django backend developer")

  if request.method == 'GET':
      people = Point.objects.all()
      serializer = PointSerializer(people, many=True)
      return JsonResponse(serializer.data, safe=False, headers=header)


