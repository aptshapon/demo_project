from django.urls import path
from image.views import ArticleListView, ArticleCreateView


urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('upload', ArticleCreateView.as_view(), name='upload'),
]