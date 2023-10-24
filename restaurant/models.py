from django.db import models
from django.contrib.auth.models import AbstractUser


class DishTypes(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    # def get_absolute_url(self):
    #     return reverse("taxi:driver-detail", kwargs={"pk": self.pk})


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    dish_type = models.ForeignKey(DishTypes, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient, related_name="dishes")
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    def __str__(self):
        return self.name
