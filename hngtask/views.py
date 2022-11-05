from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.shortcuts import render
# from .models import Point
# from .serializers import PointSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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

@api_view(['POST'])
def arth_operation(request):
    header = {"Access-Control-Allow-Origin":"*"}
    result = 0
    add_array = ['add', 'addition', 'added', 'sum', 'sumation', 'suming', 'sum up', 'adding', 'sumation of']
    minus_array = ['minus', 'subtraction','difference','remove','subtracting', 'minusing', 'subtracted', 'subtract']
    mult_array = ['mult', 'multiplication', 'multiply', 'times', 'multiplied', 'multiplying', 'timesing', 'product', 'product of', 'multiplicating']
    
    x = int(request.data["x"])
    y = int(request.data["y"])
    operation = str(request.data["operation_type"])
    split_str = operation.split(" ")
    
    for items in split_str:
      if items.lower() in add_array:
        result = x+y
        operation = "Addition"
        break
      elif items.lower() in minus_array:
        result = x-y
        operation = "Subtraction"
        break
      elif items.lower() in mult_array:
        result = x*y
        operation = "Multiplication"
        break
      else:
        operation = "invalid operator"
    new_data = {
        "slackUsername":"Timmi",
        "x":x,
        "y":y,
        "operation_type":operation,
        "result":result,
    }
    return Response(new_data, status=status.HTTP_200_OK, headers=header)





