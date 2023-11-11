from django.core.exceptions import ValidationError
from django.test import TestCase
from restaurant.forms import CookCreationForm


class DriverCreationFormTest(TestCase):
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
