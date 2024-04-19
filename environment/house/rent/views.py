from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return render(request,'home.html',{'name':'jules'})


def add(request):
  val1=request.POST["num1"]
  val2=request.POST["num2"]
  res= val1 + val2

  return render(request,"result.html",{"result":res})