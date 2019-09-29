from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def home(request):
    print("This is working")

    # get the events assigned to specific user
    # get current events
    current_events = Event.objects.filter(closed=False).order_by('-created_on')

    closed_events = Event.objects.filter(closed=True).order_by("-created_on")
    
    context = {
        "current_events": current_events,
        "closed_events": closed_events
    }
    return render(request, 'main/index.html', context)


# get the details for the events
def details(request, slug, task_id=None):
    
    volunteers = request.GET.get("volunteers")
    users = []
    if volunteers:
        users = User.objects.filter(username__icontains=volunteers)
        print(users)
    # get specific event
    event = Event.objects.get(slug=slug)

    # get task
    
    # get all tasks for each events
    tasks = Task.objects.filter(event=event)

    # taskComments = tasks.objects.get(id=id)
    # print(tasks.task_set.all())
    # taskcomments = TaskComment.objects.filter(tas=event)
    tsks = []

    for t in tasks:
        tsks.append(t)
    # check for thepost form
    if request.method == 'POST':
        for task in tasks:
            comment = request.POST.get(str(task.id))

            if comment == None:
                pass
            else:
                print(comment)

                # add it to the database
                TaskComment(task=task, posted_by=request.user, description=comment).save()
                print("Done")

    taskcomms = []
    # task comments
    taskcomments = TaskComment.objects.all().order_by('-posted_on')
    for tl in taskcomments:
        if tl.task in tsks:
            print(True)
            taskcomms.append(tl)
    context = {

        "event": event,
        "tasks": tasks,
        "taskcomments": taskcomments,
        "users": users
    }
    return render(request, 'main/details.html', context)

    
# add event
def add_event(request):
    if request.user.is_authenticated and request.user.is_superuser:
        # add event
        if request.method == "POST":

            
            # get all the data from form submit
            event_name = request.POST.get("event")
            created_by = request.user
            hits = 0

            data = Event(event_name=event_name, created_by=created_by, hits=0)
            # save the data to the database
            data.save()
            return redirect("main:home")

        else:
            form = AddEventForm()

        return render(request, 'main/add-event.html', {"form": form})

# edit event

def edit_event(request, slug):

    if request.user.is_authenticated and request.user.is_superuser:


        #  get the event to modify
        event = Event.objects.get(slug=slug)

        if request.method == 'POST':
            form = AddEventForm(request.POST, instance=event)
            if form.is_valid():
                form.save()
                return redirect("main:details", slug=event.slug)
        else:
            form = AddEventForm(instance=event)

        return render(request, 'main/add-event.html', {"form": form})

# create a new task

def add_task(request, slug):
    if request.user.is_authenticated and request.user.is_superuser:

        # get the event
        event = Event.objects.get(slug=slug)

        if request.method == 'POST':
            task_title = request.POST.get("task")

            Task(event=event, title=task_title, created_by=request.user).save()

            return redirect("main:details", slug=slug)

        return render(request, 'main/add-task.html', {"form": form})


# close the task

def close_task(request, id, slug=None):
    event = Event.objects.get(slug=slug)
    if request.user.is_authenticated and (request.user.is_superuser or request.user in event.volunteers.all()):
        # get task
        task = Task.objects.get(id=id)

        if not task.completed:
            task.completed = True
            task.save()
            return redirect("main:details", slug=slug)


# close event

def close_event(request, slug):
    if request.user.is_authenticated and request.user.is_superuser:
        # get event
        event = Event.objects.get(slug=slug)

        # check if its closed
        if not event.closed:
            event.closed = True

        event.save()
        return redirect("main:home")

# add volunteers

def add_volunteers(request, slug, user):
    if request.user.is_authenticated and request.user.is_superuser:
        # get event
        event = Event.objects.get(slug=slug)

        user = User.objects.get(username=user)

        if user not in event.volunteers.all():
            print("The user is not in the volunteers list")
            event.volunteers.add(user)
            event.save()
            return redirect("main:details", slug=slug)

# remove volunteer
def remove_volunteers(request, slug, user):
    if request.user.is_authenticated and request.user.is_superuser:
        # get event
        event = Event.objects.get(slug=slug)

        user = User.objects.get(username=user)

        if user  in event.volunteers.all():
            print("The user is  in the volunteers list")
            event.volunteers.remove(user)
            event.save()
            return redirect("main:details", slug=slug)