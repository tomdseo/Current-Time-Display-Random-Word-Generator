from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if not (request.session.get('attempt')):
        request.session['random'] = "Press \"Generate\" to generate a random word"
        request.session['attempt'] = 0
    if request.method == "POST":
        request.session['random'] = get_random_string(length=14)
        request.session['attempt'] += 1
    return render(request, "second_app/index.html")


def reset(request):
    request.session['random'] = "Press \"Generate\" to generate a random word"
    request.session['attempt'] = 0
    return redirect("/random_word")







