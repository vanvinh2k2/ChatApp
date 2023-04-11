from django.forms import ModelForm
from django import forms
from .models import ChatMessage


class ChatMessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class":"forms", "rows": 3, "placeholder": "Type message here"}))
    class Meta:
        model = ChatMessage
        fields = ["body",]