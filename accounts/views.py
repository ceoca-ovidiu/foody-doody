from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def register(request):
    if request.method == 'POST':
        print("i am on if branch")
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        user_password = request.POST['user_password']
        user_repeat_password = request.POST['user_repeat_password']
        user = User.objects.create_user(username=user_name, password=user_password, email=user_email)
        user.save()
        print("user just created")
        return redirect('/')
    else:
        print("i am on else branch")
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')
