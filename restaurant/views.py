from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import DishTypes, Dish, Ingredient, Cook


def index(request):
    """View function for the home page of the site."""

    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()

    context = {
        "num_drivers": num_cooks,
        "num_cars": num_dishes,
    }

    return render(request, "restaurant/index.html", context=context)
