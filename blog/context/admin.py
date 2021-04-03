from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE




class TutorialAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["tutorial_title", "tutorial_published"]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

#admin.site.register(Blog_Posts)
admin.site.register(Blog_Posts,TutorialAdmin)
 
