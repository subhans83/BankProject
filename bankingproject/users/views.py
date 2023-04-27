import datetime

from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views import View

from bankingapp.forms import MemberCreationForm, RegisterForm
from bankingapp.models import Register


def register_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        else:
            form = RegisterForm()
            context = {'form': form}
            return render(request, 'users/signup.html', context)

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            # return redirect('users/user_created.html')

    return render(request, 'users/signup.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'user_created.html')

        else:
            return render(request, 'users/signup.html', {'form': form})

    else:
        form = UserCreationForm()
        return render(request, 'users/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
       # login(request,user)
        if user is not None:
            print("***"+user.username)

            if Register.objects.filter(user=user.username).exists():
                return render(request, "users/user_already_registered.html")
            else:
                form = MemberCreationForm()
                login(request, user)
                # return redirect('/')
                return render(request, 'home.html', {'form': form})


        else:
            messages.info(request, "Invalid username or password")
            form = AuthenticationForm()
            return render(request, 'users/signin.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'users/signin.html', {'form': form})


def age(self):
    return int((datetime.now().date() - self.birth_date).days / 365.25)


def register(request):
    return render(request, "home.html")


def base_cv(request):
    con = {'cvs': Register.objects.all()}
    return render(request, 'users/signin.html', con)


def signout(request):
    logout(request)
    return redirect('/')
