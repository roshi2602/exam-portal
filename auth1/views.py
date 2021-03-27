from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from auth1.forms import signupForms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
# Create your views here.
def homepageview(request):
    return render(request, 'auth1/home.html')

@login_required
def javaexamsview(request):
    return render(request, 'auth1/java.html')

@login_required
def pythonexamsview(request):
    return render(request, 'auth1/python.html')

@login_required
def aptitudeexamsview(request):
    return render(request, 'auth1/aptitude.html')

@login_required
def mathsexamsview(request):
    return render(request, 'auth1/maths.html')

@login_required
def acnexamsview(request):
    return render(request, 'auth1/acn.html')

@login_required
def onlinexamsview(request):
    return render(request, 'auth1/online.html')

@login_required
def quizexamsview(request):
    return render(request, 'auth1/quiz paper.html')

@login_required
def paperexamsview(request):
    return render(request, 'auth1/online.html')




@login_required
def loginexamsview(request):
    return render(request, 'registration/login.html')

def logoutview(request):
    logout(request)
    return render(request, 'auth1/home.html')

def signupview(request):
    form=signupForms()
    if request.method=="POST":
        form =signupForms(request.POST)
    if form.is_valid():
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'auth1/signup.html', {'form':form})



