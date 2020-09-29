from django import forms

from . models import BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','text']
        labels = {'title': 'Title:','text': 'New post:'}
        widgets = {'title': '', 'text': forms.Textarea(attrs={'cols': 80})}
