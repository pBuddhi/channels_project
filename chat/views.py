from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room

@login_required
def room_view(request,room_id):
    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    # Get a list of rooms, ordered alphabetically
    print("room")
    room = Room.objects.get(pk=room_id)
    # Render that in the index template
    return render(request, "chat/room.html",{'room':room})

@login_required
def home(request):
    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    # Get a list of rooms, ordered alphabetically
    print("home")
    rooms = Room.objects.order_by("title")
    # Render that in the index template
    return render(request, "chat/index.html",{'rooms':rooms})


