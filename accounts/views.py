from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = make_password(request.POST['password'])

        user = UserProfile(username=username, email=email, password=password)
        user.save()

        return redirect('login')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = UserProfile.objects.get(username=username)
            if check_password(password, user.password):
                # Implement your login logic here
                return redirect('dashboard')
            else:
                error = 'Invalid credentials. Please try again.'
                return render(request, 'login.html', {'error': error})
        except UserProfile.DoesNotExist:
            error = 'User does not exist. Please register.'
            return render(request, 'login.html', {'error': error})

    return render(request, 'login.html')

def dashboard(request):
    # Implement your dashboard logic here
    return render(request, 'dashboard.html')

def profile(request):
    # Implement your profile logic here
    return render(request, 'profile.html')

def password_change(request):
    # Implement your password change logic here
    return render(request, 'password_change.html')

def password_reset(request):
    # Implement your password reset logic here
    return render(request, 'password_reset.html')

def email_confirmation(request):
    # Implement your email confirmation logic here
    return render(request, 'email_confirmation.html')

def logout(request):
    # Implement your logout logic here
    return render(request, 'logout.html')