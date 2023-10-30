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
    DishUpdateView,
    DishDeleteView,
    CookDeleteView,
    CookUpdateView,

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
        "dishes/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update"
    ),
    path(
        "dishes/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete"
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
        "cooks/<int:pk>/update/",
        CookUpdateView.as_view(),
        name="cook-update"
    ),
    path(
        "cooks/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete"
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
    ),

]

app_name = "restaurant"
