from django.contrib import admin
from django.contrib.admin import display

from .models import (
    Favorite,
    Ingredient,
    IngredientsInRecipe,
    Recipe,
    ShoppingCart,
    Tag,
)


class BaseAdminSettings(admin.ModelAdmin):
    """Базовая админ панель."""
    empty_value_display = '-пусто-'
    list_filter = ('author', 'name', 'tags')


class IngredientsInRecipeInline(admin.TabularInline):
    model = IngredientsInRecipe
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'name',
        'added_in_favorites'
    )
    inlines = [IngredientsInRecipeInline]
    list_filter = ['name', 'author', 'tags']
    search_fields = ['name', 'author']

    @display(description='Количество добавлений в избранное')
    def added_in_favorites(self, obj):
        return obj.favorites.all().count()


class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'measurement_unit'
    )
    list_filter = ['name']


admin.site.register(Tag)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientsInRecipe)
admin.site.register(Favorite)
admin.site.register(ShoppingCart)
