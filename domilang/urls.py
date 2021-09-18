from django.urls import path
from . import views

app_name = "domilang"
urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("home", views.home, name="home"),
    path("logout", views.logout_view, name="logout"),
    path("profile", views.profile, name="profile"),
    path("teacher", views.teacher, name="teacher"),
    path("edit", views.edit, name="edit"),
    path("inbox", views.inbox, name="inbox"),
    path("inroll", views.inroll, name="inroll"),
    path("material", views.material, name="material"),
    path("<int:module_id>", views.module, name="module"),
    path("navbar", views.navbar, name="navbar"),
    path("payments", views.payments, name="payments")
]