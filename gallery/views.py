from django.shortcuts import (render, redirect,
                              reverse, HttpResponseRedirect)
# Create your views here.


def gallery(request):
    """ A view to return the gallery page """

    template = "gallery/gallery.html"

    return render(request, template)
