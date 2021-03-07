from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Movie


class MoviesView(ListView):
    """ List of films """

    model = Movie
    queryset = Movie.objects.filter(draft=False)

    # template_name = "movies/movie_list.html"


class MovieDetailView(DetailView):
    """ Full description of the film """

    model = Movie
    slug_field = "url"
