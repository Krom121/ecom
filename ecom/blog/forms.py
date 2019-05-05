from django import forms
from .models import Comment



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form__input', 
            'placeholder': 'Your username',
            'style':'padding:1rem;font-size:1.6rem;border-radius:3px;border:none;border-bottom:2px solid green;outline:none;margin:2rem;'}),
            'email': forms.EmailInput(attrs={'class': 'form__input',
            'placeholder': 'Your email', 'style':'padding:1rem;font-size:1.6rem;border-radius:3px;border:none;border-bottom:2px solid green;outline:none;margin:2rem;'}),
            'body': forms.Textarea(attrs={'class':'form__area',
            'placeholder': 'Write your comment here', 'style':'padding:1rem;font-size:1.6rem;border-radius:3px;border:none;border-bottom:2px solid green;outline:none;margin:2rem;margin-bottom:5rem;'}),
            }