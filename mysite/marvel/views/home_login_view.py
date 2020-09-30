from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login

from .forms.login_form import LoginForm

class HomeLoginView(View):
    form_class = LoginForm
    template_name = 'marvel/home_login_template.html'

    def get(self, request, *args, **kwargs):
        
        # renderiza o formulario
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        errormessage = ''

        # verifica se o form é valido
        if form.is_valid():
            
            # verifica usuario/senha
            username = username=form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            # retorna resultado de sucesso ou falha no login
            if user is not None:
                
                # atualiza a session
                request.session.update({'username': username})
                
                # loga o usuario
                login(request, user)

                # redireciona para o Dashboard
                return HttpResponseRedirect(reverse('marvel:dashboard', args=()))
            else:
                errormessage = 'Invalid Credentials'
        else:
            errormessage = 'Invalid form data'

        # renderiza a pagina com a mensagem de erro
        return render(request, self.template_name, {'form': form, 
                                                    'errormessage': errormessage})