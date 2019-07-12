from django.shortcuts import render, HttpResponse
from datetime import datetime

def index(request):
    context = {
        "date": datetime.today().strftime('%B %d, %Y'),
        "time": datetime.today().strftime('%I:%M:%S %p')
    }

    return render(request, "first_app/index.html", context)




