from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from sending.models import Client, Mailing, Message


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MailingForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
