from django.contrib import admin
from .models import User, StudyModule, Periods

# Register your models here.

admin.site.register(User)
admin.site.register(StudyModule)
admin.site.register(Periods)