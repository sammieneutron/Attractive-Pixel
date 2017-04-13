from django.db import models

# Create your models here.
class Gallery(models.Model):
    photo = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=20)
    details = models.CharField(max_length=200)
    modal_photos = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title


class Client_showcase(models.Model):
    CATEGORY_CHOICES = (
        ('Institutions', 'Institutions'), ('Churches', 'Churches'),
        ('Organizations', 'Organizations'), ('Celebrities', 'Celebrities'),
        ('Schools', 'Schools'), ('Hospitals', 'Hospitals'),
    )
    tag_id = models.CharField(max_length=6, primary_key=True)
    photo = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    date_created = models.DateField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='')
    comments = models.CharField(max_length=200)
    number_of_views = models.IntegerField(default=0)
    number_of_likes = models.IntegerField(default=0)
    number_of_dislikes = models.IntegerField(default=0)
    client_website = models.URLField()
    modal_photos = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title
