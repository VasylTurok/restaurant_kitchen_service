from django import forms
from django.contrib.auth.forms import UserCreationForm

from restaurant.models import Cook, Dish, Ingredient


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "username",
            "years_of_experience",
            "first_name",
            "last_name",
        )


class SearchForm(forms.Form):
    search = forms.CharField(max_length=255, required=False)


class DishForm(forms.ModelForm):

    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = Dish
        fields = (
            "name",
            "description",
            "price",
            "dish_type",
            "ingredients"
        )


class CookForm(forms.ModelForm):

    class Meta:
        model = Cook
        fields = (
            "username",
            "years_of_experience",
            "first_name",
            "last_name",
        )
