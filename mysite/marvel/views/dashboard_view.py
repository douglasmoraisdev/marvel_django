from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .forms.login_form import LoginForm

class DashboardView(LoginRequiredMixin, View):
    form_class = LoginForm
    template_name = 'marvel/dashboard.html'
    login_url = '/marvel/'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        username = request.user.username
        return render(request, self.template_name, {'username': username})
