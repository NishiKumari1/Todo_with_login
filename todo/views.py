from django.shortcuts import render,redirect,get_object_or_404
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/loginn')
def home(request):
    return render(request, 'signup.html')


def signup(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        emailid=request.POST.get('emailid')
        pwd=request.POST.get('pwd')
        print(fnm,emailid,pwd)
        my_user=User.objects.create_user(fnm,emailid,pwd)
        my_user.save()
        return redirect('/loginn')
    
    return render(request, 'signup.html')    

def loginn(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        print(fnm,pwd)
        userr=authenticate(request,username=fnm,password=pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/index')
        else:
            return redirect('/loginn')
               
    return render(request, 'loginn.html')
        
@login_required(login_url='/loginn')
def index(request):
    todo=Todo.objects.all()
    if request.method=='POST':
        new_todo=Todo(
            title=request.POST['title']
        )
        new_todo.save()
        return redirect('/index')

    return render(request,'index.html',{'todos':todo})

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/index')

@login_required(login_url='/loginn')
def update(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.save()
        return redirect('/index')
    return render(request, 'index.html', {'todo': todo})


def remove_all(request):
    Todo.objects.all().delete()
    return redirect('/index')


def signout(request):
    logout(request)
    return redirect('/loginn')



