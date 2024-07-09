from django.forms import ModelForm
from .models import BlogPost
from django import forms
from froala_editor.widgets import FroalaEditor


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "body", "image"]
        widgets = {
            "body": FroalaEditor()
        }