from django.urls import path

from app import views
from app.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDetailView, ClientDeleteView, \
    MessageListView, MessageCreateView, MessageUpdateView, MessageDetailView, MessageDeleteView

app_name = 'app'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clients/add/', ClientCreateView.as_view(), name='client-create'),
    path('clients/edit/<int:pk>', ClientUpdateView.as_view(), name='client-edit'),
    path('clients/detail/<int:pk>', ClientDetailView.as_view(), name='client-detail'),
    path('clients/delete/<int:pk>', ClientDeleteView.as_view(), name='client-delete'),
    path('messages/', MessageListView.as_view(), name='message-list'),
    path('messages/add/', MessageCreateView.as_view(), name='message-create'),
    path('messages/edit/<int:pk>', MessageUpdateView.as_view(), name='message-edit'),
    path('messages/detail/<int:pk>', MessageDetailView.as_view(), name='message-detail'),
    path('messages/delete/<int:pk>', MessageDeleteView.as_view(), name='message-delete'),
]
