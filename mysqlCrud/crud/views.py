from django.forms.forms import Form
from mysqlCrud.crud.models import student
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from mysqlCrud.crud.forms import studentForm

def hello(request):
    return HttpResponse("hello")

def std(request):
    if request.method="POST":
        form=studentForm(request.POST)
        if(form.is_valid):
            try:
                form.save()
                return redirect()
            except:
                pass
        else:
            form=studentForm()
        return render(request,"",{'form':form})            
                    
