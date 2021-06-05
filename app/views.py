from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect,HttpResponse
  
# relative import of forms
from .models import crudModel
from .forms import crudForm
  
  
def create_view(request):
    context ={}
  
    form = crudForm(request.POST)
    if form.is_valid():
        form.save()
          
    context['form']= form
    return render(request, "create_view.html", context)


def list_view(request):
    context ={}

    context["dataset"] = crudModel.objects.all()
    return render(request, "list_view.html", context)


def detail_view(request, id):
    context ={}
    context["data"] = crudModel.objects.get(id = id)   
    return render(request, "detail_view.html", context)

def update_view(request, id):
    context ={}
    obj = get_object_or_404(crudModel, id = id)
    form = crudForm(request.POST, instance = obj)
  
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
    context["form"] = form
    return render(request, "update_view.html", context)

def delete_view(request, id):
    context ={}
    obj = get_object_or_404(crudModel, id = id)
  
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
  
    return render(request, "delete_view.html", context)