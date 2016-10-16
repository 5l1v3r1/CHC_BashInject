from subprocess import Popen, PIPE
import os
from django.shortcuts import render
from .models import CMSForm


# Just using function based views for now because they're easy
def cms_home(request):
    if request.method == 'POST':
        form = CMSForm(request.POST,request.FILES)
        print("Form")
        if form.is_valid():
            print("valid")
            # Put script into temp location
            filename = "tempfile"
            uploadFile(filename, request.FILES['homework'])
            # Call perl vuln
            print("Calling perl")
            ret = Popen(['perl','static/bin/cms.pm',request.POST['netid'],filename])

            # Remove temp file
            os.remove(filename)

    response = render(request, "cms.html")
    return response

def uploadFile(filename, f):
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)