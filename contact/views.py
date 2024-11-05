from django.shortcuts import render
from .models import Contact
from .forms import ContactForm


def contact_us(request):
    """
    Renders the Contact page
    """
    contact = Contact.objects.all()
    contact_form = ContactForm()

    return render(
        request,
        "contact/contact.html",
        {
            "contact_form": contact_form
        },
    )