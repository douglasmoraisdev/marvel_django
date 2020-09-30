from django import forms
from ...models.characters import Characters
from ...models.user_characters import UserCharacters

class CharacterForm(forms.Form):
    char_id = forms.IntegerField(required=True)
    char_name = forms.CharField(max_length=100, required=False)
    char_external_url = forms.CharField(max_length=500, required=False)
    image_url = forms.CharField(max_length=500, required=False)
    description = forms.CharField(max_length=500, required=False)
    avaliable_comics = forms.IntegerField(required=False)

    def add(self, request):

        char_id = self.cleaned_data['char_id']
        char_name = self.cleaned_data['char_name']
        char_external_url = self.cleaned_data['char_external_url']
        image_url = self.cleaned_data['image_url']
        description = self.cleaned_data['description']
        avaliable_comics = self.cleaned_data['avaliable_comics']


        # Verifica se o personagem já existe na base de dados
        try:
            character = Characters.objects.get(char_external_id=char_id)
        except Characters.DoesNotExist:
            # senao existe cria
            character = Characters(char_name=char_name,
                                   char_external_id=char_id,
                                   char_external_url=char_external_url,
                                   image_url=image_url,
                                   description=description,
                                   avaliable_comics=avaliable_comics
                                  )
            character.save()

        # Associa o personagem ao usuario
        user_char = UserCharacters(user=request.user.useraccount,
                                   character=character,
                                   char_user_alias=''
                                    )
        user_char.save()

        return True

    def remove(self, request):
        char_id = self.cleaned_data['char_id']

        user_char = UserCharacters.objects.get(user=request.user.useraccount,
                                               character=char_id
                                               )
        user_char.delete()

        return True

    def make_favorite(self, request):
        char_id = self.cleaned_data['char_id']

        # remove todos os favoritos
        user_chars = UserCharacters.objects.filter(user=request.user.useraccount)

        for item in user_chars:
            item.is_favorite = False
            item.save()

        # atribui favorito ao escolhido
        user_char = UserCharacters.objects.get(user=request.user.useraccount,
                                               character=char_id
                                              )
        user_char.is_favorite = True
        user_char.save()

        return True                