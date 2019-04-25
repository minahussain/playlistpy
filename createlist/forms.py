from django import forms
from .models import Playlist

class PlaylistForm(forms.ModelForm):
	class Meta:
		model = Playlist
		fields = ['origin_list_name_text']