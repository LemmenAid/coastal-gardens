from .models import Contact
from django.utils.html import format_html
from django import forms



class GardenZoneField(forms.ChoiceField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = format_html(
            'Which garden zone do you live in? '
            '<a href="#" class="zone-map-link">Check the zone map</a>'
        )


class ContactForm(forms.ModelForm):
    garden_zone = GardenZoneField(choices=Contact.ZONE_CHOICES, required=False)
    
    class Meta:
        model = Contact
        fields = ('name', 'email', 'gardening_experience', 'garden_zone', 'message')