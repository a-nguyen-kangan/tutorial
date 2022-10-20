from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random

words = ["hello", "world"]
drawnNums = []
gameSize = 100

# Create your views here.
def index(request):
    return HttpResponse("Hello world!")

@api_view()
def hello_world(request):
    words.append("blah")
    return Response(words)

@api_view()
def drawNumber(request):
    if (len(drawnNums) >= gameSize):
        return Response(f"{gameSize} numbers already drawn")
    else:
        newNum = random.randint(1, gameSize)
        while (newNum in drawnNums):
            newNum = random.randint(1, gameSize)
        drawnNums.append(newNum)
        return Response(f"Number {newNum} drawn")
   
@api_view()
def checkNum(request):
    num = request.GET.get('num')
    if (int(num) in drawnNums):
        return Response(f"{num} has been drawn")
    return Response(f"{num} hasn't been drawn")

@api_view()
def viewNums(request):
    return Response(drawnNums)

@api_view()
def resetNums(request):
    drawnNums.clear()
    return Response("Drawn numbers reset")