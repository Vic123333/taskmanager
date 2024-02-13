from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'home.html')