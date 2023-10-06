from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import SignUpForm, PostForm, ProfilePictureForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash 

@login_required
def home(request):
    user_id = request.user.id
    posts = Post.objects.filter(user_id=user_id).order_by('-created_at')
    return render(request, "customer/welcome.html", {"name": "Muzzamil", "title": "home",'posts': posts})

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


@login_required
def upload_image(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user
            form.save()
            return render(request, 'customer/upload_success.html')
    else:
        form = PostForm()
    return render(request, 'customer/upload_image.html', {'form': form})
    

def loginform(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return home(request)
        else :
            return render(request, "customer/login.html", {"error": "Invalid credentials"})
    else:
        return render(request, "customer/login.html")
    
@login_required
def options_page(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('home') 
    
    else:
        form = ProfilePictureForm(instance=request.user)

    profile_pic = request.user.profile_pic

    return render(request, 'customer/options.html', {'form': form, 'profile_pic': profile_pic})


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Update the session to reflect the password change
            update_session_auth_hash(request, user)
            return redirect('home')  # Redirect to a success page
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'customer/password_change.html', {'form': form})