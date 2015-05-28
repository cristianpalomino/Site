from django.db import models

# Create your models here.

class Actor(models.Model):
    actor_id = models.SmallIntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'actor'

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'language'

    def __str__(self):
        return '%s' % self.name


class Film(models.Model):
    film_id = models.SmallIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    language = models.ForeignKey(Language, related_name='Language')
    original_language = models.ForeignKey(Language, blank=True, null=True)
    rental_duration = models.IntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.CharField(max_length=5, blank=True, null=True)
    special_features = models.CharField(max_length=54, blank=True, null=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'film'

    def __str__(self):
        return '%s' % self.title


class FilmActor(models.Model):
    actor_id = models.ForeignKey(Actor, related_name='Actor')
    film_id = models.ForeignKey(Film, related_name='Film')
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'film_actor'
        unique_together = (('actor_id', 'film_id'),)
