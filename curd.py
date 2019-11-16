
from django.shortcuts import render, redirect
from crud.forms import *


# Create your views here.
def enter_timesheet(request):
    form = ProjectEntryForm()
    if request.method == "POST":
        form = ProjectEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/crud/show_timesheet/")

    return render(request, "crud/timesheet.html", {'form': form})

def show_timesheet(request):
    all_details = ProjectEntry.objects.all()
    return render(request, "crud/show_timesheet.html", {'projects': all_details})

def delete(request, id):
    obj = ProjectEntry.objects.get(id=id)
    obj.delete()
    return redirect("/crud/show_timesheet/")

def update(request, id):
    obj = ProjectEntry.objects.get(id=id)
    form = ProjectEntryForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("/crud/show_timesheet/")

    return render(request, "crud/timesheet.html", {'form': form})



def test(request):
    return render(request, "crud/test.html")