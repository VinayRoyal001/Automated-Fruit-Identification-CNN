from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib import messages
from users.forms import UserRegistrationForm
from users.models import UserRegistrationModel

# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from django.contrib import messages

def AdminLoginCheck(request):
    if request.method == 'POST':
        usrid = request.POST.get('username')  # Must match input field
        pswd = request.POST.get('password')   # Must match input field
        print("User ID is =", usrid)
        if usrid == 'admin' and pswd == 'admin':
            return redirect('AdminHome')  # Use redirect to named URL, not render
        else:
            messages.error(request, 'Please check your login details.')
            return redirect('AdminLogin')  # Redirect back to login page with message
    return render(request, 'AdminLogin.html')

def AdminHome(request):
    return render(request, 'admins/AdminHome.html')


def RegisterUsersView(request):
    data = UserRegistrationModel.objects.all()
    return render(request,'admins/viewregisterusers.html',{'data':data})


def ActivaUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        status = 'activated'
        print("PID = ", id, status)
        UserRegistrationModel.objects.filter(id=id).update(status=status)
        data = UserRegistrationModel.objects.all()
        return render(request,'admins/viewregisterusers.html',{'data':data})


def DeleteUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        status = 'activated'
        print("PID = ", id, status)
        UserRegistrationModel.objects.filter(id=id).delete()
        data = UserRegistrationModel.objects.all()
        return render(request, 'admins/viewregisterusers.html', {'data': data})
