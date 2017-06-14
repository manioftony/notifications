from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from masterdata.models import Student
from masterdata.forms import AddStudent
# Create your views here.


def home(request):
    obj = Student.objects.all()
    return render(request, 'list.html', locals())
    # return HttpResponse("manikanndan")


def add(request):
    form = AddStudent()
    if request.method == 'GET':
        return render(request, 'add.html', locals())
    if request.method == 'POST':
        # import ipdb;ipdb.set_trace()
        form = AddStudent(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("Error")


def delete(request, pk=None):
    obj = Student.objects.get(id=pk)
    obj.switch()
    return HttpResponseRedirect("/")



