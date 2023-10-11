from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer


class CustomerRegistrationForm(UserCreationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email= forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    passwowrd1= forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    passwowrd2= forms.CharField(label='confirm password(again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model= User
        fields= ['username','email','password1','password2']
        # labels= {'email':'Email'}
        # widgets={'username':forms.TextInput(attrs={'class':'form-control'})}



class LoginForm(AuthenticationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={'autofocus': True,  'class':'form-control'}))
    password= forms.CharField(label=('password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))




class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus': True, 'class':'form-control'}))
    new_password1 = forms.CharField(label=_('New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}),
    help_text=password_validation.
    password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('Confirm New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}))



class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','locality','city','state','zipcode']
        widgets = {'name':forms.TextInput(attrs={'class':'form-control',}),
        'locality':forms.TextInput(attrs={'class':'form-control'}),
        'city':forms.TextInput(attrs={'class':'form-control'}),
        'state':forms.TextInput(attrs={'class':'form-control'}),'zipcode':forms.Textarea(attrs={'class':'form-control'})}