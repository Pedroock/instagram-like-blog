from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import UsersProfile, UsersFollowers

class UsersRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=25, 
                               widget=forms.TextInput(attrs={'placeholder': 'Insert your username'}))  
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Insert your email'}))  
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Insert your password'}))  
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'})) 

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_username(self, *args, **kwargs):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("Username already in use")  
        return username  

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data['email'].lower()
        new  = User.objects.filter(email=email).first()
        if new is not None:
            raise ValidationError('This email is already in use')
        return email

    def clean_password2(self, *args, **kwargs):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("The two passwords must be the same")  
        return password2  

    def save(self):
        data = self.cleaned_data
        new_user = User(email=data['email'], password=data['password1'], username=data['username'])
        new_user.save()
        return new_user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[str(field)].widget.attrs.update({
                'class': f'{field}'
            })



class UsersLoginForm(forms.ModelForm):
    username_or_email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Insert your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Insert your password'}))

    class Meta:
        model = User
        fields = ['username_or_email', 'password']

    def clean(self):
        new_username_or_email = self.cleaned_data.get('username_or_email')
        print(new_username_or_email)
        new_password = self.cleaned_data.get('password')
        print(new_password)
        if '@' in new_username_or_email:
            # its a email
            new_user = authenticate(email=new_username_or_email, password=new_password)
            if new_user is not None:
                return self.cleaned_data
            else: 
                raise ValidationError('Invalid email or username')
        else: 
            # its not a email
            new_user = authenticate(username=new_username_or_email, password=new_password)
            if new_user is not None:
                return self.cleaned_data
            else: 
                raise ValidationError('Invalid email or username')
                
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[str(field)].widget.attrs.update({
                'class': f'{field}'
            })
        

class UsersProfileUpdateForm(forms.ModelForm):
    pfp = forms.ImageField(label='image')
    name = forms.CharField(widget=forms.TextInput)
    bio = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = UsersProfile
        fields = ['pfp', 'name', 'bio']

    
class UsersFollowersForm(forms.ModelForm):
    class Meta:
        model = UsersFollowers
        fields = ['follower', 'followed']