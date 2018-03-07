# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):  # For Python 2, use __unicode__ too
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):  # For Python 2, use __unicode__ too
        return self.title


class Fish(models.Model):
    name = models.CharField(max_length=128, unique=True)
    fishType = models.CharField(max_length=128)
    description = models.CharField(max_length=20000, blank=False, default="Fish Description")
    area = models.CharField(max_length=200, default="The Sea")
    sustainability = models.IntegerField(default=3)
    image = models.ImageField(upload_to='static/fish_images', blank=False)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    #user = models.ForeignKey(User)
    name = models.CharField(max_length=128, null=True)
    description = models.CharField(max_length=1280, null=True)
    ingredients = models.CharField(max_length=1280, null=True)
    method = models.CharField(max_length=9999, null=True)
    fish = models.ForeignKey(Fish)
    cost = models.FloatField(null=True)
    time = models.FloatField(default=1)
    serves = models.IntegerField(null=True)
    avgRating = models.FloatField(null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(upload_to='recipe_images', null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Review(models.Model):
    recipe = models.ForeignKey(Recipe)
    user = models.ForeignKey(User)
    rating = models.FloatField
    comment = models.CharField
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Review, self).save(*args, **kwargs)

    def __str__(self):
        return self.comment


class UserProfile(models.Model):
    # This line is requred- links UserProfile to a User model instance
    user = models.OneToOneField(User)

    # The additional attributes asked to be included
    # if using python 2.7 define __unicode__ too
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful
    def __str__(self):
        return self.user.username
