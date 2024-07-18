from django.forms import ModelForm
from .models import BlogPost
from django import forms
from froala_editor.widgets import FroalaEditor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class BlogPostForm(ModelForm):
    title = forms.CharField(
        max_length=254,
        help_text="Required. 254 characters or fewer. Letters, digits and @/./+/-/_ only.",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = BlogPost
        fields = ["title", "body", "image"]
        widgets = {"body": FroalaEditor()}


class RegistrationForm(UserCreationForm, forms.Form):
    username = forms.CharField(
        max_length=254,
        help_text="Required. 254 characters or fewer. Letters, digits and @/./+/-/_ only.",
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        ),
    )
    email = forms.EmailField(
        max_length=254,
        help_text="Required. Inform a valid email address.",
        widget=forms.EmailInput(
            attrs={"placeholder": "Email", "class": "form-control"}
        ),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "confirm password", "class": "form-control"}
        )
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        lebels = {
            "username": "Username",
            "email": "Email",
            "password1": "Password",
            "password2": "confirm password",
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.password = self.cleaned_data["password1"]
        if commit:
            user.save()
        return user

    def clean(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return self.cleaned_data


class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=254,
        help_text="Required. 254 characters or fewer. Letters, digits and @/./+/-/_ only.",
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )

    class Meta:
        model = User
        fields = ("username", "password")
        lebels = {
            "username": "Username",
            "password": "Password",
        }
