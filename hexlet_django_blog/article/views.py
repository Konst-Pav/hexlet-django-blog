from django.views import View
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.http import Http404
from hexlet_django_blog.article.models import Article


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


def index(request):
    return render(request, 'articles/index.html', context={'name': 'Articles'})


@require_http_methods(['GET', 'POST'])
def article(request, user_id):
    if request.method == 'GET':
        path = reverse('article_user_id', kwargs={'user_id': user_id})
        return render(request, 'articles/show.html', context={'user_id': user_id, 'path': path})
    else:
        raise Http404()
