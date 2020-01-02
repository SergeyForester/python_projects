from django.db import models

# Create your models here.
from django.db import models


class Room(models.Model):

    name = models.CharField(verbose_name='имя', max_length=55, unique=True)

    price = models.PositiveIntegerField(verbose_name='Цена')

    adults = models.PositiveIntegerField(verbose_name='Кол-во взрослых')

    kids = models.PositiveIntegerField(verbose_name='Кол-во детей')

    infants = models.PositiveIntegerField(verbose_name='Кол-во младенцев')

    extraPerson = models.PositiveIntegerField(verbose_name='Цена за доп. человека')

    image1 = models.ImageField(upload_to='media/rooms_img/%Y/%m/%d', blank=True)

    image2 = models.ImageField(upload_to='media/rooms_img/%Y/%m/%d', blank=True)

    description = models.TextField(verbose_name='описание номера', blank=True)



    class Meta:

        verbose_name = 'номер'

        verbose_name_plural = 'номера'



    def __str__(self):

        return self.name



class DateItem(models.Model):

    date_item = models.DateField('дата бронирования')

    room = models.ForeignKey(Room, on_delete=models.CASCADE,)

    is_busy = models.BooleanField(verbose_name='занят', default=False)



    class Meta:

        verbose_name = 'дата бронирования'

        verbose_name_plural = 'даты бронирования'



    def __str__(self):

        return str(self.date_item)





class Data(models.Model):

    nameOfText = models.CharField(max_length=70)

    valueOfText = models.CharField(max_length=5000)



class DataImages(models.Model):

    nameOfImage = models.CharField(max_length=50, default='imageName')

    image = models.ImageField()

# Create your models here.
