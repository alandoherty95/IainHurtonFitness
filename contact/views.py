from django.shortcuts import (render, redirect,
    reverse, HttpResponseRedirect)
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import ContactForm


def contact(request):
    template = "contact/contact.html"

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Message sent. We'll be in touch shortly!")
            instance = form.save()
            """ Sends automatic email confirming message was received """
            sender_email = instance.email
            subject = render_to_string(
                'contact/confirmation_emails/contact_email_subject.txt',
                {'instance': instance})
            body = render_to_string(
                'contact/confirmation_emails/contact_email_body.txt',
                {'instance': instance,
                 'contact_email': settings.DEFAULT_FROM_EMAIL})
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [sender_email],
            )

        else:
            messages.error(request, 'Message failed to send.'
                           ' Please check if the form is valid.')

    form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, template, context)
