from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse

def verify(request):
    form = UserCreationForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form=UserCreationForm

    return render(request,'accounts/verify.html',{'form':form})

def auth_login(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
        else:
            return HttpResponse("you cant")
        return HttpResponseRedirect('/')

    return render(request,'accounts/login.html')

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
