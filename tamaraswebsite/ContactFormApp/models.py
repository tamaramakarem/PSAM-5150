from django.db import models
from django.contrib.localflavor.us.models import USStateField
from django.contrib.localflavor.us.models import PhoneNumberField


class Person(models.Model):
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
    )
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	address = models.CharField(max_length=100)
	zipcode = models.DecimalField(max_digits=5, decimal_places=0)
	email = models.EmailField()
	cc_myself = models.BooleanField()
	phone = PhoneNumberField()
	subject = models.CharField(max_length=100)
	inquiry = models.CharField(max_length=1000)
	email_exists = models.BooleanField(default=False)
	has_been_answered = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.first_name
	
class Country(models.Model):
	country = USStateField() 
	population = models.BigIntegerField()
	person = models.ForeignKey('Person', related_name='countries')
	
	def __unicode__(self):
		return self.country_name

class City(models.Model):
    city = models.CharField(max_length=100)
    cities = models.ForeignKey('Person', related_name='cities') 
	
    def __unicode__(self):
        return self.name


class House(models.Model):
    house = models.ManyToManyField('City', related_name='houses')
    street = models.CharField(max_length=300)

    def __unicode__(self):
        return self.street

class Mayor(models.Model):
    mayor_name = models.CharField(max_length=100)
    city = models.ForeignKey('City', related_name='mayor', unique=True)
    house = models.ForeignKey('House')
    has_kids = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


        