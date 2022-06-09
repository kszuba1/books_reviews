from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, unique=True)
    book_title = models.CharField(max_length=50)
    book_author = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    rate = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' ' + str(self.user)

    # after add/update review it will redirect to home page
    @staticmethod
    def get_absolute_url():
        return reverse('home')

