from django.urls import path
from userauths import views

urlpatterns = [
    path('inscription/', views.register_view, name="userauths-register"),
    path('connexion/', views.login_view, name="userauths-login"),
    path('deconnexion/', views.logout_view, name="userauths-logout"),
]