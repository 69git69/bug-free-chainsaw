from django.shortcuts import render

# Create your views here.


def error_404_handler(request, exception):
    return render(request, 'pages/404.html')


def success_view(request):
    return render(request, 'pages/success.html')
