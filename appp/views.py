from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def indexView(request):
    return render(request,'index.html')

def dashboardView(request):
    return render(request, 'dashboard.html')

def loginView(request):
    return render(request, 'registration/login.html')

def registerView(request):
    # post -> form='request.post'
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        # register success -> go directly to login page
        if form.is_valid():
            form.save()
            return redirect('login_url')
    # postX -> form=''
    else:
        form=UserCreationForm()
    
    return render(request,'registration/register.html',{'form':form})


def logoutView(request):
    return render(request, 'registration/logout.html')