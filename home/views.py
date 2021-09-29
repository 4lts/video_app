from django.shortcuts import render
from django.http import HttpResponse
from decouple import config
from uploader.models import Videos

def home(request):
    videos = Videos.objects.all()
    ip_server = config('ALLOWED_HOSTS')
    return render(request, 'home_page.html', {'videos': videos[::-1], 'servidor': ip_server})

