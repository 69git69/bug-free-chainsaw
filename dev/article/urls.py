from django.urls import path
from .views import article_view, query_view, index, create_view

app_name = 'article'

urlpatterns = [
    path('', index, name='lol'),
    path('query', query_view, name='query_view'),
    path('create', create_view, name='create_view'),
    #path('success', success, name='success_view'),
    path('article/<int:id>/', article_view, name='article_view'),
]
