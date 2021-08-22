from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from .models import StudyModule, User
from django.db import IntegrityError

from .forms import LogInForm
from .forms import RegisterForm
from .forms import ProfileForm

# Create your views here.

def index(request):
    return render(request, "domilang/index.html")  

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
    return render(request, "domilang/profile.html",)

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
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            language = form.cleaned_data['native_lan']
            
            pais = form.cleaned_data['pais']
            franja = form.cleaned_data['franja']
            nivel = form.cleaned_data['nivel']
            study_lan = form.cleaned_data['study_lan']
            phone = form.cleaned_data['phone']
            if form.cleaned_data['foto']:
                foto = form.cleaned_data['foto']
                request.user.foto = foto

            request.user.first_name = first_name
            request.user.last_name = last_name
            request.user.native_lan = language
            
            request.user.pais = pais
            request.user.franja = franja
            request.user.nivel = nivel
            request.user.study_lan = study_lan
            request.user.phone = phone
            request.user.save()

            return render(request, "domilang/profile.html")
        else:
            return render(request, "domilang/edit.html",{
                "form": form
            })
    else:
        return render(request, "domilang/edit.html",{
            "form": ProfileForm(initial={
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'native_lan': request.user.native_lan,
                'foto': request.user.foto,
                'pais': request.user.pais,
                'franja': request.user.franja,
                'nivel': request.user.nivel,
                'study_lan': request.user.study_lan,
                'phone': request.user.phone
            })
        })

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