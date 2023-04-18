from django.shortcuts import render,redirect

from itestapp.models import Person


def person_detail(request):
    return render(request,'profile.html')


def logdata_fun(request):
    user_name = request.POST["txtusername"]
    user_pswd = request.POST["txtPswd"]
    return redirect('log')