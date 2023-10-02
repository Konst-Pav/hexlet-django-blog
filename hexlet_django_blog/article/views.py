from django.views import View
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.http import Http404


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'articles/index.html', context={'name': 'Articles'})


# Create your views here.
def index(request):
    return render(request, 'articles/index.html', context={'name': 'Articles'})


@require_http_methods(['GET', 'POST'])
def article(request, user_id):
    if request.method == 'GET':
        path = reverse('article_user_id', kwargs={'user_id': user_id})
        return render(request, 'articles/article.html', context={'user_id': user_id, 'path': path})
    else:
        raise Http404()
