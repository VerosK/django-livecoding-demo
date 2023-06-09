from django.http import HttpResponse

from .models import Joke

def index(request):
    return HttpResponse("Hello, world. You're at the jokes index.")


def show_joke(request, joke_id):
    the_joke = Joke.objects.get(pk=joke_id)
    return HttpResponse(the_joke.text)
