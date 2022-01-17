from django.db import models

class Book(models.Model):

    GENRE_CHOICE = (
        ('Detective', 'Detective'),
        ('Comedy', 'Comedy'),
        ('History', 'History'),
        ('Fantasy', 'Fantasy'),
        ('SelfEducation', 'SelfEducation'),
        ('Classic','Classic')
    )
    title = models.CharField(max_length=100)
    description  = models.TextField()
    image = models.ImageField(upload_to='')
    genre = models.CharField(choices=GENRE_CHOICE, max_length=100, null=True)
    data = models.DateField(auto_now_add=True, null=True)

