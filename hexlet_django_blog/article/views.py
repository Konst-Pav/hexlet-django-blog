from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.http import Http404
from django.contrib import messages
from hexlet_django_blog.article.models import Article
from .forms import ArticleForm


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        article_id = kwargs.get('id')
        return render(request, 'articles/show.html', context={
            'article': article,
            'article_id': article_id,
        })


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {
            'form': form,
            'article_id': article_id,
        })

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article updated')
            return redirect('articles')
        messages.error(request, 'Invalid data')
        return render(request, 'articles/update.html', {
            'form': form,
            'article_id': article_id,
        })


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article created')
            return redirect('articles')
        messages.error(request, 'Invalid data')
        return render(request, 'articles/create.html', {'form': form})


class ArticleFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
            messages.success(request, 'Article deleted')
        return redirect('articles')


@require_http_methods(['GET', 'POST'])
def article(request, user_id):
    if request.method == 'GET':
        path = reverse('article_user_id', kwargs={'user_id': user_id})
        return render(request, 'articles/show.html', {
            'user_id': user_id,
            'path': path,
        })
    else:
        raise Http404()
