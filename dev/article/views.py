from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import CreateArticleForm

# Create your views here.


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, "article/index.html", context)


def article_view(request, id=None):
    if id is not None:
        article = Article.objects.get(id=id)
        context = {
            'article': article,
        }
        return render(request, 'article/article_view.html', context)
    return Http404('Article Not Found')


def query_view(request):
    q = request.GET.get('q')

    try:
        q = int(q)
        article = Article.objects.get(id=q)
        context = {
            'article': article,
        }
        return render(request, 'article/article_view.html', context)

    except Exception as e:
        print("Query not found: ", e)
        q = None
        return render(request, 'article/query_view.html', )

# Older Create view
# @login_required
# def create_view(request):
#     form = CreateArticleForm()
#     context = {
#         'form': form,
#     }
#     if request.method == 'POST':
#         form = CreateArticleForm(request.POST)
#         context['form'] = form
#         if form.is_valid():
#             print(form.cleaned_data)
#             title = form.cleaned_data.get("title")
#             content = form.cleaned_data.get('content')
#             Article.objects.create(title=title, content=content)
#             return redirect('pages:success_view')
#     return render(request, 'article/create.html', context)
@login_required
def create_view(request):
    form = CreateArticleForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        print(form.cleaned_data)
        title = form.cleaned_data.get("title")
        content = form.cleaned_data.get('content')
        Article.objects.create(title=title, content=content)
        return redirect('pages:success_view')
    return render(request, 'article/create.html', context)


# def success(request):
#    return render(request, 'pages/success.html')
