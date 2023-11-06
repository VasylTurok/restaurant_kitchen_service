from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SearchForm, CookCreationForm, DishForm, CookForm
from .models import DishTypes, Dish, Ingredient, Cook


def index(request):
    """View function for the home page of the site."""

    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishTypes.objects.count()

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
    }

    return render(request, "restaurant/index.html", context=context)


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    context_object_name = "dish_list"
    template_name = "restaurant/dish_list.html"
    paginate_by = 2

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


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("restaurant:dish-list")


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm

    def get_success_url(self):
        dish_id = self.object.id
        success_url = reverse("restaurant:dish-detail", args=[dish_id])
        return success_url


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("restaurant:dish-list")


class CookCreateView(generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy('restaurant:index')

    def form_valid(self, form):
        self.object = form.save()

        login(self.request, self.object)
        return super().form_valid(form)


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    context_object_name = "cook_list"
    template_name = "restaurant/cook_list.html"
    paginate_by = 12

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


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookForm

    def get_success_url(self):
        cook_id = self.object.id
        success_url = reverse("restaurant:cook-detail", args=[cook_id])
        return success_url

    def form_valid(self, form):
        self.object.dishes.set(form.cleaned_data['dishes'])
        return super().form_valid(form)


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("restaurant:index")


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes")


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    context_object_name = "ingredient_list"
    template_name = "restaurant/ingredient_list.html"
    paginate_by = 20


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("restaurant:ingredient-list")


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("restaurant:ingredient-list")


class DishTypesListView(LoginRequiredMixin, generic.ListView):
    model = DishTypes
    context_object_name = "dish_types_list"
    template_name = "restaurant/dish_types_list.html"
    paginate_by = 20


class DishTypesCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishTypes
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish-types-list")
    template_name = "restaurant/dish_types_form.html"


class DishTypesDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishTypes
    success_url = reverse_lazy("restaurant:dish-types-list")


@login_required
def toggle_assign_to_dish(request, pk):
    cooker = Cook.objects.get(id=request.user.id)
    if (
        Dish.objects.get(id=pk) in cooker.dishes.all()
    ):
        cooker.dishes.remove(pk)
    else:
        cooker.dishes.add(pk)

    next_url = request.GET.get('next', '/')
    print(request.GET)
    return redirect(next_url)
