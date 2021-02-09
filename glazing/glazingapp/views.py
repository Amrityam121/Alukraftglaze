from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import contact
from django.core.mail import send_mail
from django.conf import settings
from .models import works_model, services
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def Home(request):
    return render(request, 'glazingapp/index.html')


def contacts(request):
    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        print(name, email, phone, message)
        send_mail(name+' '+'sent you mail', message, None,
                  [settings.EMAIL_HOST_USER], fail_silently=False)
        cont = contact(Name=name, email=email, phone=phone, message=message)
        cont.save()
        messages.success(request, 'your response has been recorded')
        return redirect('contacts')
    else:
        return render(request, 'glazingapp/contact.html')


def about(request):
    return render(request, 'glazingapp/about.html')


def works(request):
    allproj = works_model.objects.all()
    print(allproj)
    return render(request, 'glazingapp/works.html', {'allproj': allproj})


def blog(request):
    allblog = services.objects.all()
    print(allblog)
    return render(request, 'glazingapp/blog.html', {'allblog': allblog})


def Signup(request):
    if request.method == 'POST':
        user = request.POST['Username']
        Fname = request.POST['First']
        Lname = request.POST['Last']
        email = request.POST['Email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(user) > 11:
            messages.error(
                request, 'error lenght of username exceeds given range')
            return redirect('Home')

        if not user.isalnum():
            messages.error(request, 'username not alphanumeric')
            return redirect('Home')

        if pass1 != pass2:
            messages.error(request, 'password do not match')
            return redirect('Home')

        if not ('@' in email and ".com" in email):
            messages.error(request, 'Enter valid email address')
            return redirect('Home')

        myuser = User.objects.create_user(user, email, pass1)
        myuser.First_name = Fname
        myuser.Last_name = Lname
        myuser.save()
        messages.success(request, 'Acount has been sucessfully created')
        return redirect('Home')

    else:
        return HttpResponse('error 404')


def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['Loginuser']
        loginpassword = request.POST['Loginpass']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, 'sucessfully logged in')
            return redirect('Home')
        else:
            messages.error(request, 'invalid credentials!!')
            return redirect('Home')

    return HttpResponse('404-no found')


def handlelogout(request):
    logout(request)
    messages.success(request, 'sucessfully logged off')
    return redirect('Home')
