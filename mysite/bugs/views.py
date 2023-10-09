from django.http import HttpResponse
from .models import Bugs
from django.shortcuts import get_object_or_404, render

def index(request):
    latest_bug_list = Bugs.objects.order_by("-report_date")[:5]
    context = {"latest_bug_list": latest_bug_list}
    return render(request, "bugs/index.html", context)

def detail(request, bug_id):
    bug = get_object_or_404(Bugs, pk=bug_id)
    return render(request, "bugs/detail.html", {"bug": bug})

def results(request, bug_id):
    response = "You're looking at the results of bug %s."
    return HttpResponse(response % bug_id)