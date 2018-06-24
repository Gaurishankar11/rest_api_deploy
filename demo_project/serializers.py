from rest_framework import serializers
from django.contrib.postgres.fields import JSONField

class GetMovieDetailsSerializer(serializers.Serializer):
	movie_name = serializers.CharField(required = False)
	director_name = serializers.CharField(required=False)

	def validate(self, data):
		if 'movie_name' not in data and not 'director_name' in data:
			raise serializers.ValidationError({'error':'please give atleast onme input movie_name/director_name'})
		return data

class MovieDetailsSerializer(serializers.Serializer):
	movie_name = serializers.CharField()
	director_name = serializers.CharField()
	imdb_score = serializers.FloatField()
	popularity = serializers.FloatField()
	genre = serializers.ListField(child=serializers.CharField(),required=True)

class DeleteMovieDetailsSerializer(serializers.Serializer):
	movie_name = serializers.CharField()
