from django.contrib import admin
from .models import UserProfile, Note

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Note)
