from urllib.request import HTTPRedirectHandler
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegtistration
from .models import User

# Create your views here.
def base_fun(request):
    return render(request, 'base.html')

#This function will add new items and show all the items
def add_show(request):  
    if request.method == 'POST':
        fm = StudentRegtistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
    else:
        fm = StudentRegtistration()
    stud = User.objects.all()
    return render(request, 'addandshow.html', {'form':fm, 'stu':stud})

#This function will delete the items
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/addandshow/')

#This function will update the data
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegtistration(request.POST, instance = pi)
        if fm.is_valid():
            fm.save()
    else:
        pi= User.objects.get(pk=id)
        fm = StudentRegtistration(instance=pi)
    return render(request, 'updatestudent.html', {'form': fm})
        