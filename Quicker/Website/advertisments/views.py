from django.shortcuts import render , HttpResponse , redirect
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

# Create your views here.

def index(request):
    return HttpResponse("You are in your website")

def registration(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            return redirect('index/')
    else:
        form = SignUpForm()
    return render(request,'advertisments/registration.html',{'form':form})
