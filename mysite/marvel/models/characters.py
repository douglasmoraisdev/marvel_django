from django.db import models

class Characters(models.Model):

    char_name = models.CharField(max_length=100)
    char_external_url = models.CharField(max_length=100)
    created_at = models.DateTimeField('date published')
    updated_at = models.DateTimeField('date updated')


    def __str__(self):
        return f'{self.char_name}' 