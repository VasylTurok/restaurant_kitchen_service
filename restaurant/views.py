from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SearchForm
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


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    context_object_name = "dish_list"
    template_name = "restaurant/dish_list.html"
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        search = self.request.GET.get("search", "")
        context["search_form"] = SearchForm(initial={"search": search})
        return context

    def get_queryset(self):
        queryset = Dish.objects.all()
        form = SearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["search"]
            )
        return queryset
