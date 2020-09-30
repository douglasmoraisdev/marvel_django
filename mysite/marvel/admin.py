from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models.user_account import UserAccount
from .models.characters import Characters
from .models.user_characters import UserCharacters

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserAccountInline(admin.StackedInline):
    model = UserAccount
    can_delete = False
    verbose_name_plural = 'User accounts'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserAccountInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Characters)
admin.site.register(UserCharacters)