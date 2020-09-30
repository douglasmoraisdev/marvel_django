from django.db import models
from django.utils.timezone import now

from .characters import Characters
from .user_account import UserAccount

class UserCharacters(models.Model):

    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    char_user_alias = models.CharField(max_length=100, blank=True, null=True)
    is_favorite = models.BooleanField(default=False)
    added_at = models.DateTimeField('date added', default=now)

    def __str__(self):
        return f'{self.user.user.first_name} | {self.character.char_name} | {self.char_user_alias}' 