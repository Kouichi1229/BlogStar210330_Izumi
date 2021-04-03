from django import forms
from .models import *

class BlogEditForm(forms.ModelForm):
	class Meta:
		model = Blog_Posts
		fields = (
			"published_time ",
			"title",
			"content")  

		


