from django import forms

from .models import Status

class StatusModelForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            'user',
            'content'
        ]