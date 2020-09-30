from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .forms.search_character_form import SearchCharacterForm
from .forms.add_character_form import AddCharacterForm

class DashboardView(LoginRequiredMixin, View):
    form_class = SearchCharacterForm
    template_name = 'marvel/dashboard.html'
    login_url = '/marvel/'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        form_search = self.form_class()
        form_add = AddCharacterForm()

        # Renderiza as informações do Dashboard
        user_first_name = request.user.first_name
        return render(request, self.template_name, {'user_first_name': user_first_name,
                                                    'form_search': form_search,
                                                    'form_add': form_add})
