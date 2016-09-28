from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import views
from django.db.utils import OperationalError
from django.contrib.auth.hashers import make_password
import json
from CHCWebsite import settings
from .models import Home


# Just using function based views for now because they're easy
def calendar(request):
    events_json = build_events_json()
    context = {
        "events": events_json,
    }
    return render(request, "index.html", context)


def build_events_json():
    header = {"left": "prev,next today",
              "center": "title",
              "right": "month,agendaWeek,agendaDay"}
    events = []
    queryset = Home.objects.all()
    for data in queryset:
        event = {
            "title": data.title,
            "start": data.start.strftime(settings.DATE_INPUT_FORMATS),
            "end": data.end.strftime(settings.DATE_INPUT_FORMATS),
            "allDay": data.allday
        }
        events.append(event)
    result = {"header": header,
              "events": events}
    return json.dumps(result)


def registration(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
        except:
            error = True
            context = {
                "error" : error
            }
            return render(request, "registration/registration_form.html", context)
        return calendar(request)
    else:
        return render(request, "registration/registration_form.html")

def login_vuln(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(make_password(password))
        try:
            usersReturned = list(User.objects.raw("select id from auth_user where "
                                "username='" + username + "'"
                                " and password='" + make_password(password) + "'"))
        except OperationalError as err:
            usersReturned = []
            return render(request, "registration/loginvuln.html", {"errorSerious": str(err) + "\n in query \n\"\"\"" + "select id from auth_user where "
                                "username='" + username + "'"
                                " and password='" + make_password(password) + "'\"\"\""})

        if len(usersReturned) > 0:
            user = usersReturned[0]
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return calendar(request)
        else:
            return render(request, "registration/loginvuln.html", {"error": "Your username and password didn't match. Please try again."})
    else:
        return render(request, "registration/loginvuln.html")


def admin(request):
    if str(request.user) == 'admin':
        return render(request, "admin.html")
    else:
        return calendar(request)