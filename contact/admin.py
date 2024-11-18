from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin interface options for the Contact model.

    Displays fields in the Contact model, including:
    - 'gardening_experience'
    - 'garden_zone'
    - 'message'
    - 'read'

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
    """

    list_display = ('gardening_experience', 'garden_zone', 'message', 'read',)
