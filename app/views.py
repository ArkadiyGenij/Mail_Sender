from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from app.forms import ClientCreateForm, MessageCreateForm
from app.models import Client, Message


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


class MessageListView(ListView):
    model = Message
    paginate_by = 9


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(MessageMixin, CreateView):
    model = Message
    form_class = MessageCreateForm
    success_url = reverse_lazy('app:message-list')


class MessageUpdateView(MessageMixin, UpdateView):
    model = Message
    form_class = MessageCreateForm
    success_url = reverse_lazy('app:message-list')


class MessageDeleteView(MessageMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('app:message-list')
