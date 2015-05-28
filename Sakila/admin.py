from django.contrib import admin
from Sakila import models

# Register your models here.
admin.site.register(models.Actor)
admin.site.register(models.Language)
admin.site.register(models.Film)
admin.site.register(models.FilmActor)
