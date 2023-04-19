from datetime import datetime

from django.shortcuts import render
from .models import Contact
from django.shortcuts import redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from .models import Details


# Create your views here.
def index(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def uploading_data(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        user = Contact.objects.create(full_name=name, email=email, messages=message)
        user.save()
    return redirect('/')


def siteadmin(request):
    contacts = Contact.objects.all()
    return render(request, 'admin.html', {'contacts': contacts})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/contact')
        else:
            messages.info(request, 'invalid details')
            return redirect('/login')
    return render(request, 'login.html', {messages: 'messages'})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('/login')
        else:
            messages.info(request, 'Password doesnt match')
            return redirect('/register')
    return render(request, 'register.html', {messages: 'messages'})


def logout(request):
    auth.logout(request)
    return redirect('/')


def details(request):
    if request.method == 'POST':
        full_name = request.POST.get('name', '')
        dob_str = request.POST.get('dob', '')
        age = request.POST.get('age', '')
        gender = request.POST.get('gender', '')
        phonenumber = request.POST.get('phonenumber', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        district = request.POST.get('district', '')
        branch = request.POST.get('branch', '')
        accounttype = request.POST.get('account_type', '')
        
        # Convert dob_str to datetime object
        try:
            dob = datetime.strptime(dob_str, '%Y-%m-%d').strftime('%Y-%m-%d')
        except ValueError:
            dob = None
        
        # Check that dob is not None before saving the form data
        if dob is not None:
            form_details = Details.objects.create(full_name=full_name, dob=dob, age=age, gender=gender, phonenumber=phonenumber,
                                   email=email, address=address, district=district, branch=branch,
                                   accounttype=accounttype)
            form_details.save()
            messages.info(request, 'Application submitted')
        else:
            # Handle case where dob is not a valid date
            messages.info(request, 'invalid date format')
    
    return render(request, 'details.html', {messages: 'messages'})
