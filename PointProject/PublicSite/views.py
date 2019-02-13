from django.shortcuts import render, redirect
from .models import Point, Event


def index(request):
    event_list = Event.objects.all()
    point_list = Point.objects.all()

    def total_points():
        anna_count = 0
        tobin_count = 0
        total = 0
        for e in event_list:
            total += e.point.point_value
            if e.event_scoree == "AMK":
                anna_count += e.point.point_value
            elif e.event_scoree == "TDS":
                tobin_count += e.point.point_value
            else:
                anna_count += e.point.point_value
                tobin_count += e.point.point_value
        context = {"total": total, "anna": anna_count, "tobin": tobin_count}
        return context

    context = total_points()
    if len(event_list) > 4:
        event_list = event_list[len(event_list) - 5 :]
        context["event_list"] = event_list[::-1]
    else:
        context["event_list"] = event_list[::-1]
    context["point_list"] = point_list

    return render(request, "PublicSite/index.html", context)


def score(request):
    e = Event()
    p = Point()
    req = request.POST
    p.id = req["Points"]
    e.point = p
    e.event_scoree = req["Scoree"]
    e.save()

    return redirect("/")


def special(request):
    event_list = Event.objects.all()
    point_list = Point.objects.all()

    def total_points():
        anna_count = 0
        tobin_count = 0
        total = 0
        for e in event_list:
            total += e.point.point_value
            if e.event_scoree == "AMK":
                anna_count += e.point.point_value
            elif e.event_scoree == "TDS":
                tobin_count += e.point.point_value
            else:
                anna_count += e.point.point_value
                tobin_count += e.point.point_value
        context = {"total": total, "anna": anna_count, "tobin": tobin_count}
        return context

    context = total_points()
    if len(event_list) > 4:
        event_list = event_list[len(event_list) - 5 :]
        context["event_list"] = event_list[::-1]
    else:
        context["event_list"] = event_list[::-1]
    context["point_list"] = point_list

    return render(request, "PublicSite/special.html", context)


def score_special(request):
    req = request.POST
    p = Point(point_name = req["Point"], point_value = req["Value"], point_active = False)
    p.save()
    e = Event()
    e.point = p
    e.event_scoree = req["Scoree"]
    e.save()

    return redirect("/")

