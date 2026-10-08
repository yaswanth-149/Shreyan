from django.shortcuts import render, redirect

# Create your views here.

def student_list(request):
    students= [
        {
            'name': 'rahul',
            'age': 19,
            'course': 'python',
            'email': 'rahul@example.com'
        },
        {
            'name': 'vinay',
            'age': 23,
            'course': 'machine learning',
            'email': 'vinay@example.com'
        },
        {
            'name': 'priya',
            'age': 21,
            'course': 'web development',
            'email': 'priya@example.com'
        },
    ]

    return render(request, 'students/student_list.html', {
        'students': students
    })

def home(request):

    return render(request, 'students/home.html')

def login(request):

    return render(request, 'students/login.html')

# def register(request):

#     return render(request, 'students/register.html')

def contact(request):

    return render(request, 'students/contact.html')

from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import UserRegistration



def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'students/register.html')  # <-- Updated path

        # Check if email is already registered
        if UserRegistration.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return render(request, 'students/register.html')  # <-- Updated path

        # Save to SQLite database
        UserRegistration.objects.create(
            name=name,
            email=email,
            password=make_password(password)
        )

        messages.success(request, "Registration successful!")
        return redirect('register')  # Or your login view name

    return render(request, 'students/register.html')  # <-- Updated path
