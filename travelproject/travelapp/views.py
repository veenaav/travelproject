from django.shortcuts import render

# Create your views here.
def travel(request):
    return render(request,'index.html',)