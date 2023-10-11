from django.http import HttpResponse, HttpResponseRedirect
from .models import Bugs
from django.shortcuts import get_object_or_404, render

def index(request):
    latest_bug_list = Bugs.objects.order_by("-report_date")[:5]
    context = {"latest_bug_list": latest_bug_list}
    return render(request, "bugs/index.html", context)

def detail(request, bug_id):
    bug = get_object_or_404(Bugs, pk=bug_id)
    return render(request, "bugs/detail.html", {"bug": bug})

def register(request):
    if request.method == 'POST':
        description = request.POST['description']
        bug_type = request.POST['bug_type']
        status = request.POST['status']
        bug = Bugs(description=description, bug_type=bug_type, status=status)
        bug.save()

        return HttpResponseRedirect(f'/bugs/{bug.id}/')

    return render(request, "bugs/register.html")