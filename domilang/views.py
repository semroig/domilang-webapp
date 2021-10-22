from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from .models import StudyModule, User
from django.db import IntegrityError

from .forms import LogInForm
from .forms import RegisterForm
from .forms import ProfileForm

from django.core.mail import send_mail


# Create your views here.

def index(request):
    return render(request, "domilang/index2.html")  

def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("domilang:home"))
        else:
            return render(request, "domilang/login.html",{
                "message": "Invalid credentials."
            })
    else:
        return render(request, "domilang/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("domilang:index"))

def profile(request):
    return render(request, "domilang/profile.html")

def teacher(request):
    periods = [
        '10:00',
        '11:00',
        '12:00',
        '13:00',
        '14:00',
        '15:00'
    ]
    days = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
    ]
    debug = [
        True,
        False,
        True,
        True
    ]
    usuario = request.user
    available = usuario.available.all()

    listix = {}

    listix['monday'] = []
    listix['tuesday'] = []
    listix['wednesday'] = []
    listix['thursday'] = []
    listix['friday'] = []
    listix['saturday'] = []
    for ava in available:
        if ava.day == 'Monday':
            listix['monday'].append(ava.period)
        if ava.day == 'Tuesday':
            listix['tuesday'].append(ava.period)
        if ava.day == 'Wednesday':
            listix['wednesday'].append(ava.period)
        if ava.day == 'Thursday':
            listix['thursday'].append(ava.period)
        if ava.day == 'Friday':
            listix['friday'].append(ava.period)
        if ava.day == 'Saturday':
            listix['saturday'].append(ava.period)

    return render(request, "domilang/teacher.html",{
        "days": days,
        "periods": periods,
        "available": available,
        "listix": listix
    })

def home(request):
    if not request.user.is_authenticated:
        return render(request, "domilang/extranger.html")
    else:
        return render(request, "domilang/home.html")

def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        username = email
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "domilang/register.html", {
                "message": "Passwords must match."
            })
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()

            send_mail(
                'Welcome to Domilang!',
                'Hi new user! We are happy for your registration. Start paying us dollars please.',
                'admin@domilang.com',
                [email]
            )
        except IntegrityError:
            return render(request, "domilang/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("domilang:home"))
    else:
        return render(request, "domilang/register.html")

def edit(request):
    if request.method == 'POST':
        # form = ProfileForm(request.POST, request.FILES)
        if 'foto' in request.POST:
            request.user.foto = request.POST['foto']

        request.user.first_name = request.POST['first_name']
        request.user.last_name = request.POST['last_name']
        request.user.native_lan = request.POST['native_lan']
        request.user.pais = request.POST['pais']
        request.user.email = request.POST['email']
        request.user.phone = request.POST['phone']
        request.user.bio = request.POST['bio']
        #request.user.nivel = request.POST['customRadio']
        request.user.save()

        return render(request, "domilang/profile.html")
    else:
        return render(request, "domilang/edit.html")

def inbox(request):
    return render(request, "domilang/inbox.html")

def inroll(request):
    profes = User.objects.filter(role="Teacher")
    return render(request, "domilang/inroll.html",{
        "profes": profes
    })

def material(request):
    usuario = request.user
    modules = usuario.homework.all()
    return render(request, "domilang/material.html",{
        "modules": modules
    })

def module(request, module_id):
    module = StudyModule.objects.get(id=module_id)
    return render(request, "domilang/module.html",{
        "module": module
    })

def navbar(request):
    return render(request, "domilang/navbar.html")  

def payments(request):
    if not request.user.is_authenticated:
        return render(request, "domilang/extranger.html")
    else:
        return render(request, "domilang/payments.html")