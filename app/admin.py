from django.contrib import admin

from app.models import Client, Message, Newsletter, Attempt


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email',)
    search_fields = ('name', 'surname', 'email',)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'periodicity', 'status')
    search_fields = ('date_time', 'periodicity', 'status')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'status', 'response')
    search_fields = ('date_time', 'status', 'response')
