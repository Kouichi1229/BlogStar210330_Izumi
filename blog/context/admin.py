from django.contrib import admin
from .models import Blog_Posts
from tinymce.widgets import TinyMCE

class TutorialAdmin(admin.ModelAdmin):


    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }



admin.site.register(Blog_Posts,TutorialAdmin)
 
