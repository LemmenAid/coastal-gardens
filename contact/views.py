from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


def contact_us(request):
    """
    Renders the Contact page
    """

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, 
            "Contact request received! We endeavour to respond within 2 working days.")

    contact = Contact.objects.all()
    contact_form = ContactForm()

    return render(
        request,
        "contact/contact.html",
        {
            "contact_form": contact_form
        },
    )