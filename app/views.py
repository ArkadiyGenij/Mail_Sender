from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DetailView, DeleteView

from app.forms import ClientCreateForm
from app.models import Client


def dashboard(request):
    context = {
        'clients': Client.objects.count()
    }
    return render(request, 'app/dashboard.html', context)


# Create your views here.
class ClientListView(ListView):
    model = Client
    paginate_by = 10


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientCreateForm
    success_url = reverse_lazy('app:client-list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientCreateForm
    success_url = reverse_lazy('app:client-list')


class ClientDetailView(DetailView):
    model = Client


class ClientDeleteView(DeleteView):
    model = Client
    reverse_url = reverse_lazy('app:client-list')
