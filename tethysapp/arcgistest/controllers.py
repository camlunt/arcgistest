from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'arcgistest/home.html', context)

@login_required()
def bufferservice(request):
    """
    Controller for the buffer service page.
    """

    context = {}

    return render(request, 'arcgistest/bufferservice.html', context)

@login_required()
def directions(request):
    """
    Controller for the app wireframe mockups page.
    """

    context = {}

    return render(request, 'arcgistest/cool2.html', context)