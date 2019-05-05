from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Snippet


class SnippetForm(forms.ModelForm):
        class Meta:
            model = Snippet
            fields = ['name', 'email', 'message']
            widgets = {
            'name': forms.TextInput(attrs={'class':'form__input',
            'placeholder': 'Your Full Name', 'type': 'text', 'style': 'width:50%;font-size:1.5rem;padding:1rem;margin-left:2rem;display:block;margin:2rem;'}),
            'email': forms.EmailInput(attrs={'class':'form__input',
            'placeholder': 'Your Email', 'type': 'email', 'style': 'width:50%;font-size:1.5rem;padding:1rem;margin-left:2rem;display:block;margin:2rem;'}),
            'message': forms.Textarea(attrs={'class':'',
            'placeholder': 'Write Your Message Here...', 'style': 'width:50%;font-size:1.5rem;padding:1rem;margin-left:2rem;display:block;margin:2rem;'}),
            }