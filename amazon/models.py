from django.db import models
from django.utils import timezone
# from django import forms

# Create your models here.
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

# class LoginForm(forms.Form):
# 	Email = forms.CharField(max_length=254, help_text='Required. Inform a valid email address.')
# 	Password = forms.CharField(widget=forms.PasswordInput())
	 # password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(models.Model):
	UserName = models.CharField(max_length = 100)
	Email = models.CharField(max_length = 100)
	password = models.CharField(max_length = 8)
	created_date = models.DateTimeField(default = timezone.now)