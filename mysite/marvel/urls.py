from django.urls import path, include

from .views.home_login_view import HomeLoginView
from .views.dashboard_view import DashboardView
from .views.logout_view import LogoutView
from .views.search_character_view import SearchCharacterView
from .views.add_character_view import AddCharacterView

import django.contrib.auth.urls

app_name = 'marvel'
urlpatterns = [
    path('', HomeLoginView.as_view(), name='home_login'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('search_character', SearchCharacterView.as_view(), name='search_character'),
    path('add_character', AddCharacterView.as_view(), name='add_character'),

    #path('accounts/', include('django.contrib.auth.urls')),
]