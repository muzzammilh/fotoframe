from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
def home(request):
    return render(request, "customer/welcome.html", {"name": "Muzzammil", "title": "My web title"})
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            #refresh the database
            user.refresh_from_db()  
            #save user
            user.save()
            raw_password = form.cleaned_data.get('password1')
            #authenticate email password
            user = authenticate(username=user.email, password=raw_password)
            #login user
            login(request, user)
            # redirect user to home page
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'customer/signup.html', {'form': form})