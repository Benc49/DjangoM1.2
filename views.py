from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
# Create your views here.

def hey(request, name):
    return HttpResponse (f"Hey, {name}")

def age(request, end, birthyear):
    return HttpResponse(end - birthyear)

def total(request, burgers, fries, drinks):
    burgers_total = burgers * 4.50
    fries_total = fries * 1.5
    drinks_total = drinks * 1
    total = burgers_total + fries_total + drinks_total
    return HttpResponse(total)

def int(request, n):
    if abs(100 - n) <= 10:
        return HttpResponse(True)
    elif abs(200 - n) <= 10 :
        return HttpResponse(True)
    else:
        return HttpResponse(False)

def random(request, str):
        result = ""
        for i in range(len(str)):
            result = result + str[:i+1]
        return HttpResponse(result)

def lone_sum(request, a, b, c):
  if a == b and b == c:
    return HttpResponse(0)
  elif a == c:
    return HttpResponse(b)
  elif a == b: 
    return HttpResponse(c)
  elif a == c:
    return HttpResponse(b)
  elif b == c:
    return HttpResponse(a)
  elif a != b and b != c:
    return HttpResponse(a + b + c)