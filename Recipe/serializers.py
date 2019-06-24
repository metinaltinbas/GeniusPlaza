from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Recipe,User

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ('id','name','user','step','ingredient')


class RecipeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'name',
            'user',
            'step',
            'ingredients'
        ]


class RecipeUserSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.username')

    class Meta:
        model = Recipe
        fields = [
            'name',
            'user',
            'step',
            'ingredients'
        ]