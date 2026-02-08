from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Student
# Create your views here.
def index(request):
    myobj=Student.objects.all()
    context={"myobj":myobj}
    return render(request,"firstapp/index.html",context=context)
