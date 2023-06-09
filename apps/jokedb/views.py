from django.http import HttpResponse
from django.shortcuts import render

from .models import Joke


def index(request):
    return HttpResponse("Hello, world. You're at the jokes index.")


def show_joke(request, joke_id):
    context = dict(
        the_joke=Joke.objects.get(pk=joke_id)
    )
    return render(request, 'jokedb/joke_view.html', context)
