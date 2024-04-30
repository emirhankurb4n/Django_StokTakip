from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from users.forms import *
import os
from django.contrib.auth.decorators import login_required



def LoginView(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username)
            print(password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
               return render(request, "userViews/userLogin.html", {'form' : form, "error": "Username or Password is Incorrect."})
    else:
        form = CustomUserLoginForm()
    return render(request, 'userViews/userLogin.html', {'form': form})



def LogoutView(request):
    logout(request)
    return redirect('Login')



@login_required(login_url='/')
def MyProfileView(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            if not check_password(form.cleaned_data.get('current_password'), request.user.password):
                messages.error(request, 'Please enter your current password correctly.')
                return redirect('/myProfile')
            
            user = form.save(commit=False)
            if form.cleaned_data.get('new_password'):
                if form.cleaned_data.get('new_password') == form.cleaned_data.get('confirm_password'):
                    user.set_password(form.cleaned_data['new_password'])
                    user.save()
                    user_for_login = authenticate(request, username=request.user.username, password=form.cleaned_data['new_password'])
                    login(request, user_for_login)
                    messages.success(request, 'Your profile has been updated successfully with a new password.')
                    return redirect('/myProfile')
                else:
                    messages.error(request, 'New passwords entered do not match.')
                    return redirect('/myProfile')
            user.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('/myProfile')            
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'userViews/myProfile.html', {'form': form})