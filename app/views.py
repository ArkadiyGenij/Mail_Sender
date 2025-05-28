from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from app.forms import ClientCreateForm
from app.models import Client


class MessageMixin:
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Успешно!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка!')
        return super().form_invalid(form)

def dashboard(request):
    context = {
        'clients': Client.objects.count()
    }
    return render(request, 'app/dashboard.html', context)


# Create your views here.
class ClientListView(ListView):
    model = Client
    paginate_by = 10


class ClientCreateView(MessageMixin, CreateView):
    model = Client
    form_class = ClientCreateForm
    success_url = reverse_lazy('app:client-list')


class ClientUpdateView(MessageMixin, UpdateView):
    model = Client
    form_class = ClientCreateForm
    success_url = reverse_lazy('app:client-list')


class ClientDetailView(DetailView):
    model = Client


class ClientDeleteView(MessageMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('app:client-list')
