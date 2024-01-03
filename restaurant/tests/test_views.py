from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from restaurant.forms import SearchForm
from restaurant.models import Ingredient

HOME_URL = reverse("restaurant:index")
DISHES_URL = reverse("restaurant:dish-list")
COOKS_URL = reverse("restaurant:cook-list")
INGREDIENTS_URL = reverse("restaurant:ingredient-list")


class TestViewsStatusCode(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(HOME_URL)
        self.assertEqual(response.status_code, 200)

    def test_dishes_page_status_code(self):
        response = self.client.get(DISHES_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_cooks_page_status_code(self):
        response = self.client.get(COOKS_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_ingredients_page_status_code(self):
        response = self.client.get(INGREDIENTS_URL)
        self.assertNotEqual(response.status_code, 200)


class TestCooksListView(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="admin",
            password="qwerty123",
        )
        self.client.force_login(self.user)

    def test_driver_list_view(self):
        get_user_model().objects.create_user(
            username="admin2",
            password="qwerty234",
            years_of_experience=5,
        )
        response = self.client.get(COOKS_URL)
        cooks = get_user_model().objects.all()
        self.assertEqual(list(response.context["object_list"]), list(cooks))


class PrivateIngredientsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Ingredient.objects.create(name="Meet")
        Ingredient.objects.create(name="Fish")
        Ingredient.objects.create(name="Garlic")
        Ingredient.objects.create(name="Something else")

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "admin",
            "qwerty"
        )

        self.client.force_login(self.user)

    def test_create_ingredient(self):
        form_data = {
            "name": "meet",
        }

        self.client.post(reverse("restaurant:ingredient-create"), data=form_data)
        new_ingredient = Ingredient.objects.get(name=form_data["name"])

        self.assertEqual(new_ingredient.name, form_data["name"])

    def test_retrieve_ingredients(self):
        response = self.client.get(INGREDIENTS_URL)
        ingredients = Ingredient.objects.all()
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["ingredient_list"]),
            list(ingredients)
        )
