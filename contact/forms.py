from django import forms
from django.utils.html import format_html
from .models import Contact


class GardenZoneField(forms.ChoiceField):
    """
    Custom form field that represents the garden zone selection.

    This field provides a custom label that includes a link to a zone map
    and is used in the ContactForm to allow users to select their gardening zone.

    Attributes:
        label (str): The label displayed for the field, including a hyperlink.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = format_html(
            'Which garden zone do you live in? '
            '<a href="#" class="zone-map-link">Check the zone map</a>'
        )


class ContactForm(forms.ModelForm):
    """
    Form for capturing contact information and gardening-related inquiries.

    This form is used to collect a user's name, email, gardening experience,
    garden zone, and a message. The garden zone field is presented as a custom
    choice field with a link to a zone map.

    Attributes:
        garden_zone (GardenZoneField): Custom field for selecting the gardening zone.
    """
    garden_zone = GardenZoneField(choices=Contact.ZONE_CHOICES, required=False)
    
    class Meta:
        model = Contact
        fields = ('name', 'email', 'gardening_experience', 'garden_zone', 'message')