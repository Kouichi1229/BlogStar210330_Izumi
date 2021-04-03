from django import forms
from .models import *
from datetime import datetime

class BlogEditForm(forms.ModelForm):
	class Meta:
		model = Blog_Posts
		fields = (
			"title",
			"content")  

		


