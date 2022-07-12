from django.contrib import admin
from .models import Goal
from .models import AuthtokenToken
from .models import Messages
from .models import Supporter

admin.site.register(Goal)
admin.site.register(AuthtokenToken) # work in progress
admin.site.register(Messages)
admin.site.register(Supporter)