from django.contrib import admin
from .models import registieren, forum, forumanswer


admin.site.register(registieren)
admin.site.register(forum)
admin.site.register(forumanswer)