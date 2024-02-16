from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):

    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            # authenticate
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You Have Been Logged In")
                return redirect('home')
            else:
                messages.success(request, "There Was An Error Logging In")
                return redirect('home')
    else:
         return render(request, 'home.html')


def logoutUser(request):
    logout(request)
    messages.success(request, "You Have Been Logged out!")
    return redirect("home")
    