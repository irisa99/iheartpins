from django.contrib import admin
# from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Address, Person, TradeCredits, Profile,User


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'is_verified',
        'created_at',
    )

admin.site.register(Profile, ProfileAdmin)


class UserAdmin(BaseUserAdmin):
    list_display = (
        'username',
        'email',
        'last_login',
        'user_last_edit',
        'user_date_created',
        'is_active',
        'is_superuser',
        'is_admin',
    )
    search_fields = ('username', 'email',)
    readonly_fields = ('last_login', 'user_last_edit', 'user_date_created')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, UserAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'firstname',
        'lastname',
    )

admin.site.register(Person, PersonAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'person',
        'is_shipping',
        'is_billing',
        'is_inactive',
        'street1',
        'street2',
        'city',
        'state',
        'postalcode',
    )
    list_filter = ['is_inactive',]

admin.site.register(Address,AddressAdmin)
admin.site.register(TradeCredits)
