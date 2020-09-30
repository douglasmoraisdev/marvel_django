from django.db import models
from django.contrib.auth.models import User
from .characters import Characters

class UserAccount(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    favorite_character = models.ForeignKey(Characters, on_delete=models.CASCADE,  blank=True, null=True)

    def __str__(self):
        return self.user.first_name