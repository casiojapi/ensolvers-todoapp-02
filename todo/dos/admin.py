from django.contrib import admin

from .models import *

# register "Do" in admin to test via admin panel

admin.site.register(Do)