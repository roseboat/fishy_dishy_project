# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

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
    
    user = models.CharField(max_length=128, null=True)
    def __unicode__(self):
        return self.name
    
    name = models.CharField(max_length=128, null=True)
    description = models.CharField(max_length=9999, null=True)
    ingredients = models.CharField(max_length=9999, null=True)
    method = models.CharField(max_length=9999, null=True)
    fish = models.ForeignKey(Fish)
    time = models.IntegerField(null=True)
    serves = models.IntegerField(null=True)
    avgRating = models.FloatField(null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(upload_to='recipe_images', blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.time<=0:
            self.time=1
        if self.serves<=0:
            self.serves=1
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Review(models.Model):
    recipe = models.ForeignKey(Recipe)
    user = models.ForeignKey(User)
    rating = models.IntegerField(blank=True, default = 5)
    comment = models.CharField(max_length=2000, null=True)
    date_posted = models.DateTimeField(auto_now=True)

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
