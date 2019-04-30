from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User
# from django import forms

# Create your models here.
class Register(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
# class login(models.Model):
# 	Name = models.CharField(max_length=50)
# 	Password = models.VarCharField(max_length=8)

# class clothe(models.Model):

# 	Product = models.CharField(max_length = 50)
# 	Price = models.IntegerField()
	# footware = models.ForeignKey('footware', default = 1)
   # phonenumber = models.IntegerField()

	# class Meta:
	# 	db_table = "clothe"

# class footware(models.Model):

# 	Product = models.CharField(max_length = 50)
# 	Price = models.IntegerField()
	# phonenumber = models.IntegerField()

	# class Meta:
 #  		db_table = "footware"

# class accessories(models.Model):

# 	Product = models.CharField(max_length = 50)
# 	Price = models.IntegerField()
   # phonenumber = models.IntegerField()

	# class Meta:
	# 	db_table = "accessories"
