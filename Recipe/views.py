from rest_framework import generics, mixins , permissions
from rest_framework.response import Response

from .models import Recipe,Step,User
from .serializers import RecipeSerializer,RecipeCreateSerializer,RecipeUserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.views.generic.edit import  UpdateView, DeleteView



class RecipeListAPIView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer



class RecipeCreateAPIView(mixins.CreateModelMixin,generics.ListAPIView):

    serializer_class = RecipeCreateSerializer
    queryset = Recipe.objects.all()

    def post(self,request,*args,**kwargs):

        return self.create(request,*args,**kwargs)

    def create(self, request, *args, **kwargs):

        my_token = self.request.META.get('HTTP_AUTHORIZATION').split()[1]
        user_id = Token.objects.get(key=my_token).user_id
        userx = get_object_or_404(User,id=user_id)
        ownership = Recipe(user=userx)
        serializer = self.serializer_class(ownership, data=request.data)


        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeByUserAPIView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeUserSerializer

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = [
        'name',
        'user',
        'step',
        'ingredients'
    ]


class RecipeDelete(DeleteView):
    model = Recipe
