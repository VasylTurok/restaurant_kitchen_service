from django.urls import path

from .views import (
    index,
    DishListView,
    CookCreateView,
    CookListView,
    CookDetailView,

)

urlpatterns = [
    path("", index, name="index"),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list"
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
        "cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"
    ),

]

app_name = "restaurant"
