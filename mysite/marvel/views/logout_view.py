from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        
        # desloga o usuario
        logout(request)

        return HttpResponseRedirect(reverse('marvel:home_login', args=()))

