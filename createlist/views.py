from django.shortcuts import render, redirect
from .models import Playlist
from .forms import PlaylistForm
from django.contrib import messages

from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


def index(request):
	# find playlist search
	if request.method == "POST":
		form = PlaylistForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items = Playlist.objects.all
			messages.success(request, ('Playlist Added!'))
			return render(request, "index.html", {'all_items': all_items})
	else:
		all_items = Playlist.objects.all
		return render(request, "index.html", {'all_items': all_items})


def logout(request):
    auth_logout(request)
    return render_to_response('index.html', {}, RequestContext(request))

def delete(request, list_id):
	item = Playlist.objects.get(pk=list_id)
	item.delete()
	messages.success(request, ('Playlist has been deleted'))
	return redirect('index')