from django.urls import path
from hngtask import views

urlpatterns = [
    path('', views.point_list),
]