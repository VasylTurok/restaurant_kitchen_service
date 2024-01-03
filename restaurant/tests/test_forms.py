from django.core.exceptions import ValidationError
from django.test import TestCase
from restaurant.forms import (
    CookCreationForm,
    SearchForm,
    DishForm,
    CookForm
)
from restaurant.models import Ingredient, DishTypes, Cook


class CookCreationFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.form_data = {
            "first_name": "test First",
            "last_name": "test Last",
            "username": "test_username",
            "password1": "test12345",
            "password2": "test12345",
            "years_of_experience": 2
        }

    def test_cook_creation_form_with_firs_last_name_years_of_experience(self):
        form = CookCreationForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, self.form_data)


class SearchFormTest(TestCase):
    def test_search_form_valid(self):
        form_data = {"search": "query"}
        form = SearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_search_form_empty(self):
        form_data = {"search": ""}
        form = SearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_search_form_max_length(self):
        form_data = {"search": "a" * 256}
        form = SearchForm(data=form_data)
        self.assertFalse(form.is_valid())


class DishFormTest(TestCase):
    def setUp(self):

        self.ingredient1 = Ingredient.objects.create(name="Ingredient 1")
        self.ingredient2 = Ingredient.objects.create(name="Ingredient 2")

    def test_dish_form_valid(self):
        dish_type = DishTypes.objects.create(name="Main Course")
        cook = Cook.objects.create(username="chef123", years_of_experience=5, first_name="John", last_name="Doe")

        form_data = {
            "name": "Dish Name",
            "description": "Description of the dish",
            "price": 10.99,
            "dish_type": dish_type.id,
            "ingredients": [self.ingredient1.id, self.ingredient2.id]
        }
        form = DishForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_form_invalid(self):

        form_data = {
            "name": "Dish Name",
            "description": "Description of the dish",
            "price": 10.99,
            "dish_type": "Invalid Type",
            "ingredients": [self.ingredient1.id, self.ingredient2.id]
        }
        form = DishForm(data=form_data)
        self.assertFalse(form.is_valid())


class CookFormTest(TestCase):
    def test_cook_form_valid(self):
        form_data = {
            "username": "chef123",
            "years_of_experience": 5,
            "first_name": "John",
            "last_name": "Doe",
        }
        form = CookForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_cook_form_missing_field(self):
        form_data = {
            "username": "chef123",
            "first_name": "John",
        }
        form = CookForm(data=form_data)
        self.assertFalse(form.is_valid())