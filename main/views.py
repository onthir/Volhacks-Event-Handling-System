from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def home(request):
    print("This is working")

    # get current events
    current_events = Event.objects.filter(closed=False)

    context = {
        "current_events": current_events
    }
    return render(request, 'main/index.html', context)


# get the details for the events
def details(request, slug):
    # get specific event
    event = Event.objects.get(slug=slug)

    context = {

        "event": event
    }
    return render(request, 'main/details.html', context)

    
# add event
def add_event(request):
    if request.user.is_authenticated and request.user.is_superuser:
        # add event
        if request.method == "POST":
            form = AddEventForm(request.POST, request.FILES)
            if form.is_valid():

                # get all the data from form submit
                data = form.save(commit=False)
                data.created_by = request.user
                data.hits = 0

                # save the data to the database
                data.save()
                return redirect("main:home")

            else:
                print("Something went wrong")
        else:
            form = AddEventForm()

        return render(request, 'main/add-event.html', {"form": form})