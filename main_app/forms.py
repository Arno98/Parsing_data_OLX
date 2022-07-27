from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин', 'autocomplete': False, 'name': 'username'}),)
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'current-password', 'placeholder': 'Пароль', 'name': 'password'}),)

