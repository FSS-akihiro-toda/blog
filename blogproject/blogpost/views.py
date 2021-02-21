from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views.generic.edit import CreateView
from .models import BlogModel
from django.urls import reverse_lazy
# Create your views here.

# 一覧


class BlogList(ListView):
    template_name = 'list.html'
    model = BlogModel

# 詳細


class BlogDetail(DetailView):
    template_name = 'detail.html'
    model = BlogModel

# 新規作成


class BlogCreate(CreateView):
    template_name = 'create.html'
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')

# 削除


class BlogDelete(DeleteView):
    template_name = 'delete.html'
    model = BlogModel
    success_url = reverse_lazy('list')

# 更新


class BlogUpdate(UpdateView):
    template_name = 'update.html'
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')
