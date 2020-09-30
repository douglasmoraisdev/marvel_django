from django.urls import path, include

from .views.home_login_view import HomeLoginView
from .views.dashboard_view import DashboardView
from .views.logout_view import LogoutView

import django.contrib.auth.urls

app_name = 'marvel'
urlpatterns = [
    path('', HomeLoginView.as_view(), name='home_login'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]