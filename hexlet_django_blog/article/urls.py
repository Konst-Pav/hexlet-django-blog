from django.urls import path
from hexlet_django_blog.article import views


urlpatterns = [
    path('', views.index),
    path('<int:user_id>/', views.article, name='article_user_id'),
]
