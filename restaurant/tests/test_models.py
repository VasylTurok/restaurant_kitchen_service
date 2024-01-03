from django.contrib.auth import get_user_model
from django.test import TestCase

from restaurant.models import Dish, DishTypes


class ModelTests(TestCase):
    def setUp(self) -> None:
        username = "admin1"
        password = "1234wdfgh"
        years_of_experience = "5"
        first_name = "qwe"
        last_name = "rty"

        self.dish_type = DishTypes.objects.create(
            name="fast food"
        )

        self.cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            years_of_experience=years_of_experience,
        )
        self.dish = Dish.objects.create(
            name="Pizza",
            description="Some description",
            price=100,
            dish_type=self.dish_type
        )

    def test_dish_str_method(self):
        dish = self.dish
        self.assertEqual(str(dish), "Pizza")

    def test_cook_str(self):
        cook = self.cook
        self.assertEqual(
            str(self.cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})",
        )
