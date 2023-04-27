from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from datetime import date
# Create your views here.


from django.shortcuts import render, redirect, get_object_or_404

from .forms import MemberCreationForm, RegisterForm
from .models import Register, Branch


def index(request):
    return render(request, "index.html")

def create_view(request):
    form = MemberCreationForm()
    if request.method == 'POST':
        form = MemberCreationForm(request.POST)


        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user.username  # The logged-in user

            portfolio.save()

            return redirect('bankingapp:register_success')
    return render(request, 'home.html', {'form': form})


def register_success(request):
    return render(request, "register_success.html")

def user_created(request):
    return render(request,"user_created.html")

def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')


# AJAX
def load_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'branch_dropdown_list_options.html', {'branches': branches})
