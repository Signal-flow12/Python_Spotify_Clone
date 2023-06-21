from django.shortcuts import render
from.models import Artist
from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name ="home.html"
    
class About(TemplateView):
    template_name = "about.html"

class SongList(TemplateView):
    template_name = "song_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["songs"] = songs # this is where we add the key into our context object for the view to use
        return context

class Song:
    def __init__(self, title, album):
        self.title = title
        self.album = album

songs = [
    Song("Lost", "stressed and depressed"),
    Song("Do it for the stunt", "No clue album")
]

class ArtistList(TemplateView):
    template_name = "artist_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["artists"] = Artist.objects.filter(name__icontains=name)
        else:
            context["artists"] = Artist.objects.all()
        return context
