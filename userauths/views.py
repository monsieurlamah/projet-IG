from django.shortcuts import render, redirect
from userauths.form import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from userauths.models import User

def register_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "Vous êtes déjà connecté !")
        return redirect("app-home")
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Salut, {username} votre compte est créé avec succès !')
            new_user = authenticate(email = form.cleaned_data['email'], password = form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('app-home')
    else:
        form = UserRegisterForm()
    context ={
        'form':form
    }
    return render(request, 'userauths/register.html', context)

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Vous êtes avec succès !")
                return redirect('app-home')
            else:
                messages.warning(request, "L'email ou le mot de passe est incorrect !")
                return redirect('userauths-connexion')
        except:
            messages.warning(request, "L'utilisateur n'existe pas !")
            return redirect("userauths-connexion")
    if request.user.is_authenticated:
        messages.warning(request, "Vous êtes déjà connecté !")
        return redirect('app-home')
    return render(request, 'userauths/connexion.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Vous êtes déconnecté avec succès !')
    return redirect("app-home")

