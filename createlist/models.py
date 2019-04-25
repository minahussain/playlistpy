from django.db import models
from django.utils import timezone
from django import forms
import datetime

SONG_TYPES = (
		'kept',
		'deleted',
		'added',
	)

# class User(User):
# 	def __str__(self):
# 		return self.username

class Playlist(models.Model):
	# _id = models.AutoField(primary_key=True)
	origin_list_name_text = models.CharField(max_length=200)
	# origin_list_author_text = models.CharField(max_length=200)
	# change_date = models.DateTimeField('recent change date')
	# def was_edited_today(self):
	# 	return self.change_date >= timezone.now() - datetime.timedelta(days=1)

	def __str__(self):
		return self.origin_list_name_text 


class Song(models.Model):
	name_text = models.CharField(max_length=200)
	author_text = models.CharField(max_length=200)
	_type = forms.ChoiceField(label='Filter', required=True, choices=SONG_TYPES)
	change_date = models.DateTimeField('recent change date')

	def __str__(self):
		return self.name_text + ' by ' + self.author_text \
				+ ' (' + self._type + ') '