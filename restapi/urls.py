from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.hello_world, name='hello'),
    path('bingo/draw', views.drawNumber, name='drawNumber'),
    path('bingo/check', views.checkNum, name='checkNum'),
    path('bingo/view', views.viewNums, name='viewNums'),
    path('bingo/reset', views.resetNums, name='resetNums'),
]