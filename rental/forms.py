from django import forms
from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'email', 'phone', 'equipment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'mail@example.ru'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'xxx-xxx-xxx'}),
            'equipment': forms.HiddenInput(),
        }