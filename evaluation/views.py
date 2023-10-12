from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import Movie


def mars(request):
    return render(request, 'movies.html', {'movies': ['back to the future', 'x-men']})


def data(request):
    data = Movie.objects.all()
    return render(request, 'movies.html', {'movies': data})


def detail(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404('Movie does not exist')
    data = Movie.objects.get(pk=id)
    return render(request, 'detail.html', {'movie': data})


def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')

    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/api')

    return render(request, 'add.html')


def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404('Movie does not exist')
    movie = Movie.objects.get(pk=id).delete()
    return HttpResponseRedirect('/api')


def home(request):
    return HttpResponse("Home page")
