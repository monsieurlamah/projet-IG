from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Nom d'utilisateur", 'class': 'form-input form-wide'}),
                                   error_messages={'required':"Veuillez entrer un nom d'utilisateur."})
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': "E-mail", 'class': 'form-input form-wide'}),
                             error_messages={'required':'Veuillez entrer une adresse E-mail.'})
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Mot de passe', 'class': 'form-input form-wide'}), 
                                error_messages={'required': 'Veuillez entrer un mot de passe.'})
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"La confirmation du mot de passe", 'class': 'form-input form-wide'}),
                                error_messages={'required': "Veuillez entrer une confirmation du mot de passe."})
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        