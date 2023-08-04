from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import SignUpForm

def home(request):
    return render(request, "customer/welcome.html", {"name": "Muzzamil", "title": "Home Page"})

def SignUpView(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "customer/signup.html", {"form": form})

def LoginView(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return render(request, "customer/welcome.html", {"name": "Muzzamil", "title": "Home Page"})
    else:
        return render(request, "customer/login.html")

