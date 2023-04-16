from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Tags)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)