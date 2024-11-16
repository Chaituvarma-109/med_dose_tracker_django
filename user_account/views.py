from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

from user_account.forms import SignupForm, LoginForm


def signup(request):
    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('home')

    context = {"form": form,}
    return render(request, 'user_account/signup.html', context=context)


def login_(request):
    form = LoginForm()

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'There is an error in Logging, please check email and password')
            return redirect(request, 'login')


    context = {"form": form, }
    return render(request, 'user_account/login.html', context=context)


def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'tracker/index.html')
