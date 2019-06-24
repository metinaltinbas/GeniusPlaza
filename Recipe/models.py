from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):

    class Meta(object):
        unique_together = ('email','username')


class Step(models.Model):
    step_text = models.CharField(max_length=255,null=False)

class Ingredient(models.Model):
    text = models.CharField(max_length=255,null=False)


class Recipe(models.Model):
    name = models.CharField(max_length=255,null=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    step = models.ForeignKey(Step,on_delete=models.SET_NULL,null=True)
    ingredient = models.ForeignKey(Ingredient,on_delete=models.SET_NULL,null=True)