from django.urls import path
from .views import success_view

app_name = 'pages'
urlpatterns = [
    path('success', success_view, name='success_view'),
]
