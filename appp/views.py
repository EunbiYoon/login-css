from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# index templates
def indexView(request):
    return render(request,'index.html')


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


# dashboard templates
@login_required(login_url='login_url')
def bomView(request):
    return render(request,'dash_bom.html')