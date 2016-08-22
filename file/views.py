from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Folder, Receipt
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

total = Folder.objects.all().aggregate(receipt_total=Sum('receipt__amount'))

class IndexView(generic.TemplateView):
    template_name = 'file/index.html'


class DetailView(generic.DetailView):
    model = Folder
    template_name = 'file/details.html'

    def get_total(self):
        total = Folder.objects.filter(self).aggregate(Sum('receipt__amount'))
        return total

# >>>>>>> FOLDER VIEWS >>>>>>>>


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

# >>>>>>> RECEIPT VIEWS >>>>>>>>>>>>


class ReceiptCreate(CreateView):
    model = Receipt
    fields = ['folder', 'store', 'date', 'amount']


class ReceiptUpdate(UpdateView):
    model = Receipt
    fields = ['store', 'date', 'classification']


class ReceiptDelete(DeleteView):
    model = Receipt
    success_url = reverse_lazy('file:folders')


class UserFormView(View):
    form_class = UserForm
    template_name = 'file/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('file:index')

        return render(request, self.template_name, {'form': form})
