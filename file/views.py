from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Folder
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
# from .forms import UserForm


class IndexView(generic.TemplateView):
    template_name = 'file/index.html'


class DetailView(generic.DetailView):
    model = Folder
    template_name = 'file/details.html'


class MyFoldersView(generic.ListView):
    template_name = 'file/folders.html'
    context_object_name = 'all_folders'

    def get_queryset(self):
        return Folder.objects.all()


class FolderCreate(CreateView):
    model = Folder
    fields = ['name']


class FolderUpdate(UpdateView):
    model = Folder
    fields = ['name']


class FolderDelete(DeleteView):
    model = Folder
    success_url = reverse_lazy('file:folders')


