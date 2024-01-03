from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from restaurant.models import DishTypes, Ingredient, Cook, Dish


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience", )
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("years_of_experience", )}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "years_of_experience",
                    )
                },
            ),
        )
    )


@admin.register(DishTypes)
class DishTypesAdmin(admin.ModelAdmin):
    search_fields = ("model",)
    list_filter = ("name",)


admin.site.register(Ingredient)

admin.site.register(Dish)
