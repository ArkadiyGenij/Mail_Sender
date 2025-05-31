from django import forms

from app.models import Client, Message, Newsletter


class StyleFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientCreateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MessageCreateForm(StyleFormMixin, forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': '20', }), label='Сообщение')

    class Meta:
        model = Message
        fields = '__all__'


class NewsletterCreateForm(StyleFormMixin, forms.ModelForm):

    date_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Newsletter
        fields = ['date_time', 'periodicity', 'clients', 'message']
