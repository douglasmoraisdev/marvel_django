from django.db import models
from .characters import Characters
from .user_account import UserAccount

class UserCharacters(models.Model):

    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    char_user_alias = models.CharField(max_length=100)
    added_at = models.DateTimeField('date added')

    def __str__(self):
        return f'{self.user.user.first_name} | {self.character.char_name} | {self.char_user_alias}' 