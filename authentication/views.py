from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm

def home(request):
    return render(request, 'authentication/home.html', {})

def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, ('Log in Success'))
            return redirect('home')
        else:
            messages.success(request, ('Error Logging In - Please Try Again...'))

            return redirect('login')
    else:
        return render(request, 'authentication/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('Logout success..'))

    return redirect('home')

def register_user(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Authenticate User
            user = authenticate(request, username=username, password=password)
            # Login user
            login(request, user)
            messages.success(request, ('You have Registered...'))
            return redirect('home')
    else:
        form = SignUpForm()

    context = { 'form' : form } 

    return render(request, 'authentication/register.html', context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, ('Profile Updated successfully.'))
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)

    context = { 'form' : form } 

    return render(request, 'authentication/edit_profile.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('Password Updated successfully.'))
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)

    context = { 'form' : form } 

    return render(request, 'authentication/change_password.html', context)