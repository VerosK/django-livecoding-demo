# apps/jokedb/admin.py

from django.contrib import admin
from .models import Joke

class JokeAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'is_profane')
    list_filter = ['pub_date', 'is_profane']
    search_fields = ['text']

admin.site.register(Joke, JokeAdmin)
