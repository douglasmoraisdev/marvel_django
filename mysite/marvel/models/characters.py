from django.db import models
from django.utils.timezone import now

class Characters(models.Model):

    char_name = models.CharField(max_length=100)
    char_external_id = models.IntegerField(default=0)
    char_external_url = models.CharField(max_length=100)
    created_at = models.DateTimeField('date published', default=now)
    updated_at = models.DateTimeField('date updated', default=now)


    def __str__(self):
        return f'{self.char_name}' 