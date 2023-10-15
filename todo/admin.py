from django.contrib import admin
from .models import Task


# Overwrite the Admin Page to show additional Fields for a Model
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "task",
        "is_completed",
        "updated_at",
    )
    search_fields = ("task",)


# Register your models here.
admin.site.register(Task, TaskAdmin)
