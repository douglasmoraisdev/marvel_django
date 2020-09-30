from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .forms.add_character_form import AddCharacterForm

class AddCharacterView(LoginRequiredMixin, View):
    form_class = AddCharacterForm
    template_name = 'marvel/dashboard.html'
    login_url = '/marvel/'
    redirect_field_name = 'redirect_to'

    def post(self, request, *args, **kwargs):
        errormessage = ''
        data = []

        search_result = {}
        if 'char_name' in request.POST:
            form = AddCharacterForm(request.POST)
            if form.is_valid():
                add_result = form.add(request)

                return render(request, self.template_name, {'errormessage': errormessage})

