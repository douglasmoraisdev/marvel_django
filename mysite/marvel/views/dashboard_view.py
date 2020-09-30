from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .forms.search_character_form import SearchCharacterForm
from .forms.character_form import CharacterForm

from ..models.user_characters import UserCharacters

class DashboardView(LoginRequiredMixin, View):
    form_class = SearchCharacterForm
    template_name = 'marvel/dashboard.html'
    login_url = '/marvel/'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        form_search = self.form_class()
        form_add = CharacterForm()
        my_characters = []

        # Renderiza as informações do Dashboard
        user_first_name = request.user.first_name
        user_characters = UserCharacters.objects.filter(user=request.user.useraccount)

        for item in user_characters:
            my_characters.append({'char_external_url': item.character.char_external_url,
                                  'image_url': item.character.image_url,
                                  'char_name': item.character.char_name,
                                  'description': item.character.description,
                                  'avaliable_comics': item.character.avaliable_comics,
                                  'is_favorite': item.is_favorite,
                                  'char_id': item.character.id
                                })           

        return render(request, self.template_name, {'user_first_name': user_first_name,
                                                    'my_characters': my_characters,
                                                    'form_search': form_search,
                                                    'form_add': form_add})
