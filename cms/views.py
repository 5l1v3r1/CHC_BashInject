from subprocess import Popen, PIPE
import os
from django.shortcuts import render
from .models import CMSForm


# Just using function based views for now because they're easy
def cms_home(request):
    context = {}
    # The netid being non-alphanumeric is checked client side, they should
    # notice because of the difference between the error messages for
    # no-file and netid
    if request.method == 'POST':
        form = CMSForm(request.POST,request.FILES)
        context['form'] = form
        if form.is_valid():
            # Put script into temp location
            filename = "tempfile"
            uploadFile(filename, request.FILES['homework'])
            # Call perl vuln
            Popen(['perl','static/bin/cms.pm',request.POST['netid'],filename])
            context["saved"] = "Saved "+request.POST['netid']+".zip"

    response = render(request, "cms.html", context=context)
    return response


def uploadFile(filename, f):
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)