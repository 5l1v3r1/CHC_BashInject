from subprocess import Popen, PIPE
import os
from django.shortcuts import render
from django.utils.encoding import smart_str
from django.http import HttpResponse
import mimetypes
from wsgiref.util import FileWrapper
from .models import CMSForm

HW_PATH = "hwfiles"

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
            Popen(['perl','../static/bin/cms.pm',request.POST['netid'],filename],cwd=HW_PATH)
            context["saved"] = "Saved "+request.POST['netid']+".zip"
            # Now generate report
            try:
                with open(os.path.join(HW_PATH,request.POST['netid']+"_report.txt"),"w") as f:
                    f.write("There are no grading comments at this time, check back later!")
            except:
                context['error'] = "Error writing report: "+os.path.join(HW_PATH,request.POST['netid']+"_report.txt")
    elif 'netid' in request.GET:
        netid = request.GET['netid']
        netid_path = os.path.join(HW_PATH,netid+"_report.txt")
        if os.path.exists(netid_path):
            return send_file(request,netid_path)
        else:
            context['error'] = "No such netid report found"

    response = render(request, "cms.html", context=context)
    return response


def uploadFile(filename, f):
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def send_file(request,path):
    """
    Send a file through Django without loading the whole file into
    memory at once. The FileWrapper will turn the file object into an
    iterator for chunks of 8KB.
    """
    wrapper = FileWrapper(open(path, "r"))
    content_type = mimetypes.guess_type(path)[0]

    response = HttpResponse(wrapper, content_type=content_type)
    response['Content-Length'] = os.path.getsize(path)  # not FileField instance
    response['Content-Disposition'] = 'attachment; filename=%s' % \
                                      smart_str(os.path.basename(path))  # same here
    print(smart_str(os.path.basename(path)))
    return response