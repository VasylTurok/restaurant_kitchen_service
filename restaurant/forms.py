from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class SearchForm(forms.Form):
    search = forms.CharField(max_length=255, required=False)