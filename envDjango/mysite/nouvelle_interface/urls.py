from django.urls import path
from . import views

urlpatterns = [
    path('acceuil/', views.index, name='acceuil'),
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('connect/', views.login_view, name='connecter'),
]
