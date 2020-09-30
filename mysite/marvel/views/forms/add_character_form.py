from django import forms
from ...models.characters import Characters
from ...models.user_characters import UserCharacters

class AddCharacterForm(forms.Form):
    char_id = forms.IntegerField(required=True)
    char_name = forms.CharField(max_length=100, required=True)
    char_external_url = forms.CharField(max_length=500, required=True)
    image_url = forms.CharField(max_length=500, required=False)    

    def add(self, request):
        char_id = self.cleaned_data['char_id']
        char_name = self.cleaned_data['char_name']
        char_external_url = self.cleaned_data['char_external_url']
        image_url = self.cleaned_data['image_url']

        # Verifica se o personagem já existe na base de dados
        try:
            character = Characters.objects.get(char_external_id=char_id)
        except Characters.DoesNotExist:
            # senao existe cria
            character = Characters(char_name=char_name,
                                   char_external_id=char_id,
                                   char_external_url='',
                                   image_url=image_url
                                  )
            character.save()

        # Associa o personagem ao usuario
        user_char = UserCharacters(user=request.user.useraccount,
                                   character=character,
                                   char_user_alias=''
                                    )
        user_char.save()

        return True