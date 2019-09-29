from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def home(request):
    print("This is working")

    # get current events
    current_events = Event.objects.filter(closed=False).order_by('-created_on')

    context = {
        "current_events": current_events
    }
    return render(request, 'main/index.html', context)


def task_inidiv(event, slug, id):
    event = Event.objects.get(slug=slug)

    # get the task
    tasks = Task.objects.filter(event=event)

    singleTask = tasks.get(id=id)
    taskComments = TaskComment.objects.filter(task=singleTask)
 
    return taskComments
# get the details for the events
def details(request, slug, task_id=None):
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
        "taskcomments": taskcomments
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
            form = AddTaskForm(request.POST or None)

            if form.is_valid():
                data = form.save(commit=False)
                data.event = event
                data.created_by = request.user
                data.save()
                return redirect("main:details", slug=event.slug)
        else:
            form = AddTaskForm()
        return render(request, 'main/add-task.html', {"form": form})
