from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Notes

# Create your views here.

def index(request, pk):
    notes = Notes.objects.all()
    return render(request, 'index.html', {'notes':notes, 'pk':pk})


def create(request, pk):
    if request.method == 'POST':

        title = request.POST['title']
        description = request.POST['description']
        
        if title == '' and description == '':
            return redirect('http://127.0.0.1:8000/index'+pk)
        
        elif title != '' and description == '':
            messages.info(request, 'Please enter a description')
            return redirect('create')
        
        elif title == '' and description != '':
            messages.info(request, 'Please enter a title')
            return redirect('create')
        
        else:

            note = Notes(title=title,description=description, username=pk)
            note.save()
            messages.info(request,'Note created successfully')
            return redirect('http://127.0.0.1:8000/index/'+pk)


    else:
        return render(request, 'create.html',{'pk':pk})


def delete(request, title):
    note = Notes.objects.get(title=title)
    name = note.username
    note.delete()
    messages.info(request,'Note deleted successfully')
    return redirect('http://127.0.0.1:8000/index/'+name)


def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users':users})

def find(request):
    name = request.POST['username']
    if not User.objects.filter(username=name).exists():
        User.objects.create_user(username=name).save()
    user = auth.authenticate(username=name)
    return redirect('http://127.0.0.1:8000/index/'+name)

def logout(request):
    auth.logout(request)
    return redirect('http://127.0.0.1:8000/')