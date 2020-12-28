from django.views import generic
from django.shortcuts import redirect

from .models import Article
# from .forms import ArticleForm


class ArticleListView(generic.ListView):
    model = Article


class ArticleCreateView(generic.CreateView):
    model = Article
    fields = ('image',)
    # template_name = "article_list.html"
    # form_class = ArticleForm
    # success_url = '/thanks/'

