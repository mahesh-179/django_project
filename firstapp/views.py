from django.shortcuts import render
from .forms import StudentForm
from .models import Studentdata1  # IMPORTING MODEL

def home(request):
    my_obj=Studentdata1.objects.all()
    context={"my_obj":my_obj}
    return render(request,"firstapp/frontend.html",context=context)
def admin(request):
    return render(request,"http://127.0.0.1:8000/admin")

def index(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
           Studentdata1.objects.create(
                name=form.cleaned_data["ename"],
                age=form.cleaned_data["age"],
                add=form.cleaned_data["add"],
                gpa=form.cleaned_data["gpa"],
               college=form.cleaned_data["college"],
            )
    context = {"form": form}
    return render(request, "firstapp/form.html",context=context)
