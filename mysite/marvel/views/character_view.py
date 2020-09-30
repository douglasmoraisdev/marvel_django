from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


from .forms.character_form import CharacterForm

class CharacterView(LoginRequiredMixin, View):
    form_class = CharacterForm
    template_name = 'marvel/dashboard.html'
    login_url = '/marvel/'
    redirect_field_name = 'redirect_to'

    def post(self, request, *args, **kwargs):
        errormessage = ''

        # delete character
        if request.POST['_method'] == "DELETE":
            form = CharacterForm(request.POST)
            if form.is_valid():
                remove_result = form.remove(request)

                return HttpResponseRedirect(reverse('marvel:dashboard', args=()))
            else:
                return render(request, self.template_name, {'errormessage': 'error on delete character'})
        
        # make favorite
        elif request.POST['_method'] == 'PUT':
            form = CharacterForm(request.POST)
            if form.is_valid():
                favorite_result = form.make_favorite(request)

                return HttpResponseRedirect(reverse('marvel:dashboard', args=()))
            else:
                return render(request, self.template_name, {'errormessage': 'error on make favorite'})


        # add character
        elif 'char_name' in request.POST:
            form = CharacterForm(request.POST)
            if form.is_valid():
                add_result = form.add(request)

                return HttpResponseRedirect(reverse('marvel:dashboard', args=()))
            else:
                return render(request, self.template_name, {'errormessage': errormessage})

