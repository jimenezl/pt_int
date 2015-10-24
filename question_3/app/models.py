"""Models for this Django app"""

from django.db import models

class Movies(models.Model):
    """Model for the movies table in the database"""

    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    year = models.TextField()
    genre = models.TextField()

    def space_free_title(self):
        return self.title.replace(' ', '_')

    def __unicode__(self):
        return self.title

    class Meta:
        """Meta class for Movies model"""

        managed = True
        db_table = 'movies'
