from django.urls import path

from articles import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('<slug:slug>', views.article_item, name='article_detail'),
    path('create/', views.article_create, name='create'),
]
