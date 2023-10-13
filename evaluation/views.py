from lib2to3.pgen2.driver import Driver
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse
from .serializers import MovieSerializer
from .models import Movie
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


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


@api_view(['POST', 'GET'])
def MovieJson(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse({'message': 'Movie list displayed successfully ', 'results': serializer.data}, safe=False)

    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'message': 'Movie created successfully', 'results': serializer.data}, status=status.HTTP_201_CREATED)
    return Response({'message': 'Method ('+request.method+') entered is not allowed.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def MovieJson_Detail(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except Movie.DoesNotExist:
        return Response({'message': 'Movie does not exists'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response({'message': 'Movie displayed successfully', 'results': serializer.data}, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        movie.delete()
        return Response({'message': 'Movie has been delete sucessfully'}, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Movie has been updated sucessfully', 'results': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Method ('+request.method+') entered is not allowed.'}, status=status.HTTP_400_BAD_REQUEST)
