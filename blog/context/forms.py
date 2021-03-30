from django import forms
from .models import Blog_Posts
from tinymce.models import HTMLField

class BlogEditForm(forms.ModelForm):
	class Meta:
		model = Blog_Posts
		fields = [  
			"published_time ",
			"title",
			"content"		
			]
			
				
