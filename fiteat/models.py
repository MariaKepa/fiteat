# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Category(models.Model):
	name = models.CharField(max_length=200)
	pathtopicture = models.CharField(max_length=200, default= '')

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Product(models.Model):
	name = models.CharField(max_length=200)
	category = models.ForeignKey(Category)
	protein = models.FloatField(default=0.0)
	carbon = models.FloatField(default=0.0)
	fats = models.FloatField(default=0.0)
	calories = models.FloatField(default=0.0)

	def __str__(self):
		return self.name


class DiaryEntry(models.Model):
	product = models.ForeignKey(Product)
	user = models.ForeignKey('auth.User')
	weight = models. IntegerField(default=0)
	published_date = models.DateTimeField(
            blank=True, null=True)

	def __str__(self):
		return str(self.id)

