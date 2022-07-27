from django.urls import path, include
from . import views

app_name = 'main_app'
urlpatterns = [
	path('', views.index, name='index'),
	path('logout', views.logout_user, name='logout_user'),
	path('update', views.update, name='update'),
	path('delete', views.delete, name='delete'),
]
