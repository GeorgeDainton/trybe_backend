from django.contrib import admin
from .models import Goal
from .models import AuthtokenToken


admin.site.register(Goal)
admin.site.register(AuthtokenToken) # work in progress

