from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse
from .serializers import MovieSerializer
from .models import Movie
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db import connection
import re

# ################################### API ZIP CODE ###################################
@api_view(['GET'])
def ZipCodeJson(request):
    zip_code = request.GET.get('zp')
    if request.method == 'GET':
        if zip_code is not None and not re.match(r'^\d+$', zip_code):
            return Response({'message': 'Please input a number value for zip code (zp) to execute API correctly.'}, status=status.HTTP_400_BAD_REQUEST)
        if zip_code is None:
            return Response({'message': 'Please input a value different to null for zip code (zp) to execute API correctly.'}, status=status.HTTP_400_BAD_REQUEST)

        with connection.cursor() as cursor:
            query = "select  zp.d_codigo,  zp.d_ciudad,  zp.c_estado,  zp.d_estado,  zp.id_asenta_cpcons,  zp.d_asenta, zp.d_zona,  zp.d_tipo_asenta,  zp.c_mnpio, zp.d_mnpio from evaluation_zipcode zp where zp.d_codigo = %s"
            cursor.execute(query, [zip_code])
            data = cursor.fetchall()

            transformed_data = {}

            for item in data:
                zip_code = item[0]
                locality = item[1]
                federal_identity_key = item[2]
                federal_identity_name = item[3]
                federal_identity_code = None
                settlements_key = item[4]
                settlements_name = item[5]
                settlements_zone_type = item[6]
                settlements_type_name = item[7]
                municipality_key = item[8]
                municipality_name = item[9]

                if zip_code not in transformed_data:
                    transformed_data[zip_code] = {
                        "zip_code": zip_code,
                        "locality": locality,
                        "federal_identity": {
                            "key": federal_identity_key,
                            "name": federal_identity_name,
                            "code": federal_identity_code,
                        },
                        "settlements": [],
                        "municipality": {
                            "key": municipality_key,
                            "name": municipality_name
                        }
                    }

                settlement_data = {
                    "key": settlements_key,
                    "name": settlements_name,
                    "zone_type": settlements_zone_type,
                    "settlement_type": {"name": settlements_type_name}
                }

                transformed_data[zip_code]["settlements"].append(
                    settlement_data)

        if not transformed_data:
            return Response({'message': 'No data found', 'data': []}, status=status.HTTP_404_NOT_FOUND)
        else:
            results = transformed_data[zip_code]
            return Response({'message': 'Data fetched successfully', 'data': results}, status=status.HTTP_200_OK)


# ################################### Learning Django ###################################
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
