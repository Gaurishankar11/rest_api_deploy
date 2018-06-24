# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import (api_view, permission_classes, renderer_classes)
from .models import *
from .serializers import *
from .decorator import superuser_only
from rest_framework.response import Response
from django.http import HttpResponse

# Create your views here.
@api_view(['POST'])
def get_movie_details(request):
	result = {}
	serializer = GetMovieDetailsSerializer(data=request.data)
	if not serializer.is_valid():
		return HttpResponse(serializer.errors['error'])

	data = serializer.validated_data

	try:

		if 'movie_name' in data:
			res = movie_details.objects.filter(movie_name = data['movie_name']).values_list('movie_name','director_name','imdb_score','popularity','genre')
		elif 'director_name' in data:
			res = movie_details.objects.filter(director_name = data['director_name']).values_list('movie_name','director_name','imdb_score','popularity','genre')

		if res:
			result['movie_name'] = res[0][0]
			result['director_name'] = res[0][1]
			result['imdb_score'] = res[0][2]
			result['popularity'] = res[0][3]
			result['genre'] = res[0][4]

		return Response(result)

	except Exception as e:
		return HttpResponse(str(e))

@api_view(['POST'])
@superuser_only
def add_movie_details(request):
	serializer = MovieDetailsSerializer(data=request.data)
	if not serializer.is_valid():
		return HttpResponse(serializer.errors['errors'])

	data = serializer.validated_data

	try:
	
		new_movie = movie_details(**data)
		new_movie.save()

		return HttpResponse('success')

	except Exception as e:
		return HttpResponse(str(e))


@api_view(['PUT'])
@superuser_only
def edit_movie_details(request):
	serializer = MovieDetailsSerializer(data=request.data)
	if not serializer.is_valid():
		return HttpResponse(serializer.errors['errors'])

	data = serializer.validated_data

	try:

		movie_details.objects.filter(movie_name = data['movie_name']).update(**data)

		return HttpResponse('success')

	except Exception as e:
		return HttpResponse(str(e))

@api_view(['POST'])
@superuser_only
def delete_movie_details(request):

	serializer = DeleteMovieDetailsSerializer(data=request.data)
	if not serializer.is_valid():
		return HttpResponse(serializer.errors['errors'])

	data = serializer.validated_data

	try:

		movie_details.objects.filter(movie_name = data['movie_name']).delete()

		return HttpResponse('success')

	except Exception as e:
		return HttpResponse(str(e))
