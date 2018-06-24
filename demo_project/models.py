# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class movie_details(models.Model):
	movie_name = models.TextField(primary_key=True)
	director_name = models.TextField()
	imdb_score = models.FloatField()
	popularity = models.FloatField()
	genre = ArrayField(ArrayField(models.TextField()))

	def __str__(self):
		return str(self.movie_name)