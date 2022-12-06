from django import forms

from . import models


class TinyMessageForm(forms.ModelForm):
    content = forms.CharField(label="Mensagem", widget=forms.TextInput)

    class Meta:
        model = models.TinyMessage
        fields = [
            'content'
        ]