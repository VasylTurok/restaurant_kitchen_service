from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SearchForm, CookCreationForm
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


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class CookCreateView(generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        self.object = form.save()

        login(self.request, self.object)
        return super().form_valid(form)


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    context_object_name = "cook_list"
    template_name = "restaurant/cook_list.html"
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        search = self.request.GET.get("search", "")
        context["search_form"] = SearchForm(initial={"search": search})
        return context

    def get_queryset(self):
        queryset = Cook.objects.all()
        form = SearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["search"]
            )
        return queryset


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes")


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    context_object_name = "ingredient_list"
    template_name = "restaurant/ingredient_list.html"
    paginate_by = 20


class DishTypesListView(LoginRequiredMixin, generic.ListView):
    model = DishTypes
    context_object_name = "dish_types_list"
    template_name = "restaurant/dish_types_list.html"
    paginate_by = 20
