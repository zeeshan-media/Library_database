from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import Book
from .models import Crud
from django.contrib.auth.models import auth

# Create your views here.


def add_show(request):
    if request.method == 'POST':
        fm= Book(request.POST)
        if fm.is_valid():
            fm.save()
            fm = Book()
    else:
        fm=Book()
    bk=Crud.objects.all()
    return render(request,'crud/addandshow.html', {'form': fm, 'bk': bk})


def deletes(request,book_id):
    if request.method == "POST":
        dl=Crud.objects.get(pk=book_id)
        print(dl)
        dl.delete()
    return redirect('addandshow')


def updates(request,book_id):
    if request.method=="POST":
        up=Crud.objects.get(pk=book_id)
        fm=Book(request.POST, instance=up)
        if fm.is_valid():
            fm.save()
    else:
        up=Crud.objects.get(pk=book_id)
        fm=Book(instance=up)

    return render(request,"crud/updatebook.html" ,{'form':fm})

def log_out(request):
    auth.logout(request)
    return redirect('/')