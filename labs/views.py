from django.shortcuts import render, redirect
from .models import *


from django.contrib import messages

# auths
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'reports.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credetials Invalid')
            return redirect('/login')
    else:
        return render(request, 'login.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')