from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from fotis.albums.models import Album

def index(request):
    year_list = Album.objects.all().order_by('-year')
    return render_to_response('albums/index.html', {'year_list': year_list})

def year(request, year):
    try:
        y = Album.objects.get(year=year)
    except Album.DoesNotExist:
        raise Http404
    return render_to_response('albums/year.html', {'year': y})

def event(request, year, event):
    return HttpResponse("This is " + year + "  " + event)
