from django import forms

from . import models


class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        # fields = ['title', 'slug', 'body', 'thumbnail']
        fields = ['title', 'body', 'thumbnail']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'thumbnail']
        labels = {
            "title": "Title",
            "body": "Text",
            "thumbnail": "Thumbnail"
        }
        widgets = {
            "title": forms.TextInput(attrs={'placeholder': 'Write article title', 'class': 'form-control mb-3'}),
            "body": forms.TextInput(attrs={'placeholder': 'Write article text', 'class': 'form-control mb-3'}),
            "thumbnail": forms.TextInput(attrs={'class': 'form-control mb-3'})
        }