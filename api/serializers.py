# serializers.py

from rest_framework import serializers
from .models import Ingredients, Recipe

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ['name', 'quantity', 'unit']
        # read_only_fields=['id']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, required=False)
    class Meta:
        model = Recipe

        fields = ['id','title','ingredients','description','instructions']
        read_only_fields = ['id']

    def _get_or_create_ingredients(self, ingredients, recipe):
        for ingredient in ingredients:
            ingredients_obj, create = Ingredients.objects.get_or_create(**ingredient)
            recipe.ingredients.add(ingredients_obj)


    def create(self, validated_data):
        """Create Recipe"""
        ingredients = validated_data.pop('ingredients',[])
        recipe = Recipe.objects.create(**validated_data)
        self._get_or_create_ingredients(ingredients,recipe)
        return recipe