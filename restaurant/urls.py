from django.urls import path

from .views import (
    index,
    DishListView,
    CookCreateView,
    CookListView,
    CookDetailView,
    DishDetailView,
    IngredientListView,
    DishTypesListView,

)

urlpatterns = [
    path("", index, name="index"),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list"
    ),
    path(
        "dishes/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail"
    ),
    path(
        "registration/",
        CookCreateView.as_view(),
        name="registration"
    ),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cook-list"
    ),
    path(
        "cooks/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail"
    ),
    path(
        "ingredients",
        IngredientListView.as_view(),
        name="ingredient-list"
    ),
    path(
        "dish_types",
        DishTypesListView.as_view(),
        name="dish-types-list"
    )

]

app_name = "restaurant"
