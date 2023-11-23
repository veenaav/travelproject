from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo1(request):
    return render(request,'addvalues.html')

def calculate(request):
    x=int(request.GET['number1'])
    y=int(request.GET['number2'])
    add=x+y
    sub=x-y
    multi=x*y
    div=x/y

    return render(request,'result.html',{'res1':add,'res2':sub,'res3':multi,'res4':div})
