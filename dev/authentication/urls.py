from django.urls import path
from .views import register_view, login_view, logout_view

app_name = 'authentication'
urlpatterns = [
    path('', register_view, name='register'),
    path('register', register_view, name='register_view'),
    path('login', login_view, name='login_view'),
    path('logout', logout_view, name='logout_view'),
    #path('success', success, name='success_view'),
]
