from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .forms import LoginForm
from .parsing_data import ads_collection

def index(request):
	if request.method != 'POST':
		form = LoginForm()
		return render(request, 'main_app/index.html', {'form': form})
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			authenticate_user = authenticate(username=request.POST['username'], password=request.POST['password'])
			if authenticate_user is None:
				return render(request, 'main_app/index.html', {'form': form, 'error': 'Неверный логин или пароль!'})
			else:
				login(request, authenticate_user)
				return redirect('main_app:index')

def logout_user(request):
	logout(request)
	return redirect('main_app:index')

def update(request):
	ads = ads_collection()
	ads = zip(ads[0], ads[1], ads[2])
	if request.is_ajax():
		return JsonResponse({'data': render_to_string('main_app/ads.html', context={'ads': ads}, request=request)})

def delete(request):
	if request.is_ajax():
		return JsonResponse({'delete': 1})
