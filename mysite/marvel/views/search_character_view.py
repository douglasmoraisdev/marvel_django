from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .forms.search_character_form import SearchCharacterForm

class SearchCharacterView(LoginRequiredMixin, View):
    form_class = SearchCharacterForm
    template_name = 'marvel/dashboard.html'
    login_url = '/marvel/'
    redirect_field_name = 'redirect_to'

    def post(self, request, *args, **kwargs):
        errormessage = ''
        data = []
        form = self.form_class()

        search_result = {}
        if 'char_name_search' in request.POST:
            form_search = SearchCharacterForm(request.POST)
            if form_search.is_valid():
                search_result = form_search.search()

                # se encontrou resultado na api
                if search_result['success']:

                    # parse dos dados dos personagens
                    for results in search_result['data']['results']:

                        external_id = results['id']
                        name = results['name']
                        description = results['description']
                        image = results['thumbnail']['path']
                        image += '.'+results['thumbnail']['extension']
                        comics_available = results['comics']['available']
                        comics_list = [items['name'] for items in results['comics']['items']]
                        resources = [items for items in results['urls']]

                        data.append({ 'external_id': external_id,
                                'name': name,
                                'description': description,
                                'image': image,
                                'comics_available': comics_available,
                                'comics_list': comics_list,
                                'resources': resources
                        })
                else:
                    errormessage = search_result['message']

        return render(request, self.template_name, {'form_search': form, 
                                                    'user_first_name': request.user.first_name,
                                                    'errormessage': errormessage, 
                                                    'search_result': data})

