# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=200)
	pathtopicture = models.CharField(max_length=200, default= '')

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=200)
	category = models.ForeignKey(Category)
	protein = models.FloatField(default=0.0)
	carbon = models.FloatField(default=0.0)
	fats = models.FloatField(default=0.0)

	def __str__(self):
		return self.name
