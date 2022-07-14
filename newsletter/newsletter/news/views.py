from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import News
from .forms import NewsForm


class NewsHome(ListView):
    model = News
    template_name = 'news.html'
    ordering = ['-date_created']


class NewsDetail(DetailView):
    model = News
    template_name = 'news_detail.html'


class CreateNews(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'create_news.html'
    #fields = '__all__'


class UpdateNews(UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'update_news.html'
    #fields = '__all__'


class DeleteNews(DeleteView):
    model = News
    template_name = 'delete_news.html'
    success_url = reverse_lazy('home')
