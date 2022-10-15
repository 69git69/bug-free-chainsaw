from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def register_view(request):

    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        print(dir(user))
        return redirect("authentication:login_view")

    context = {
        "form": form
    }
    return render(request, "authentication/register.html", context)

# Old Login form
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is None:
#             return render(request, 'authentication/login.html', {"error": "Invalid credentials"})
#         login(request, user)
#         return redirect('article:lol')
#     return render(request, 'authentication/login.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('article:lol')
    else:
        form = AuthenticationForm(request)
    context = {
        'form': form,
    }
    return render(request, "authentication/login.html", context)

def logout_view(request):
    logout(request)
    return redirect('article:lol')
