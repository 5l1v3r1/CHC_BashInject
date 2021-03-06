from django.contrib.auth.models import User
from django.shortcuts import render
from .models import FAQ
from django.db.models import Q
from django.db.utils import OperationalError

# Just using function based views for now because they're easy
def faq_home(request):
    user = request.user

    # if request.method == 'POST' and request.user.is_authenticated:
    #     question = request.POST['query']
    #     newQ = FAQ.objects.create(title=question, user=str(user))
    #     newQ.save()
    #     newQ.id
    #
    #     print "Created with id" + str(newQ.id)
    #
    #     # driver = webdriver.PhantomJS()  # or add to your PATH
    #     # driver.get('http://youcanthack.me:1234/login/')
    #     # username = driver.find_element_by_name("username")
    #     # password = driver.find_element_by_name("password")
    #     # username.send_keys("admin")
    #     # password.send_keys("CHCL33t")
    #     # username.submit();
    #     # driver.get('http://youcanthack.me:1234/faq/?id=' + str(newQ.id))
    #     # driver.save_screenshot('screen.png')

    if "id" in request.GET:
        try:
            queryset = list(FAQ.objects.raw("select id, title, user, answer from faq_faq where id=" + request.GET["id"]))
            error = None
        except OperationalError as err:
            queryset = FAQ.objects.all()
            error = str(err) + "\n in query \n\"\"\"" + \
                     "select id, title, user, answer from faq_faq where id=" + request.GET["id"] + "\"\"\""
    else:
        queryset = FAQ.objects.all()
        error = None



    # if str(user) != 'admin':
    #     queryset = queryset.filter(Q(user__exact=str(user)) | Q(user__exact='admin'))
    # else:
    #     if "id" in request.GET:
    #         idToCheck = request.GET["id"]
    #         queryset = queryset.filter(Q(id__exact=idToCheck))

    context = {
        "questions": queryset,
        "username": user,
        "errorSerious": error
    }

    if "id" in request.GET:
        context["showq"] = 1

    response = render(request, "faq.html", context)
    #response['X-XSS-Protection'] = 0
    return response