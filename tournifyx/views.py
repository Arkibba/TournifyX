from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import TournamentForm
import secrets
import string
import random

# Views
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 != password2:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'auth/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
            return render(request, 'auth/register.html')

        user = User.objects.create_user(username=username, password=password1, email=email)
        user.save()

        # Automatically create UserProfile
        UserProfile.objects.create(user=user)

        # Optional: Also create a HostProfile now, or later when they choose to host
        HostProfile.objects.create(user=user)

        messages.success(request, 'Registration successful! Please log in.')
        return redirect('login')

    return render(request, 'auth/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, '')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password!')
            return render(request, 'auth/login.html')

    return render(request, 'auth/login.html')


@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('login')


@login_required(login_url='login')
def host_tournament(request):
    try:
        host_profile = HostProfile.objects.get(user=request.user)
    except HostProfile.DoesNotExist:

        host_profile = HostProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            tournament = form.save(commit=False)

            tournament.created_by = host_profile

            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            while Tournament.objects.filter(code=code).exists():
                code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

            tournament.code = code
            tournament.save()

            messages.success(request,
                             f"Tournament '{tournament.name}' created successfully! Players can join with code: {tournament.code}")
            return redirect('home',)
    else:
        form = TournamentForm()

    return render(request, 'host_tournament.html', {'form': form})



