from django.shortcuts import render
from .models import CMSForm

# Just using function based views for now because they're easy
def cms_home(request):
    if request.method == 'POST': #and request.user.is_authenticated:
        form = CMSForm(request.POST,request.FILES)
        if form.is_valid():
            filename = request.POST['netid']
            uploadFile(filename, request.FILES['file'])

    response = render(request, "cms.html")
    return response

def uploadFile(filename, f):
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)