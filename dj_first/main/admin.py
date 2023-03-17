from django.contrib import admin
from .models import Task
from django.forms.models import  BaseInlineFormSet


# class ProfileInline(admin.StackedInline):
#     """
#     Allows profile to be added when creating user
#     """
#     model = Task
#
#
# class UserProfileAdmin(admin.ModelAdmin):
#     """
#     Options for the admin interface
#     """
#     inlines = [ProfileInline]

admin.site.register(Task)






