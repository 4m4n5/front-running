import datetime

from django.db import models
from django.utils import timezone
# Create your models here.
class AppleCustomerOrder(models.Model):
	trade_id = models.PositiveIntegerField(primary_key=True, null=False)
	customer_id = models.PositiveIntegerField()
	trade_type = models.CharField(max_length=200, null=False)
	security_type = models.CharField(max_length=200, null=False)
	security_name = models.CharField(max_length=200, null=False)
	price = models.FloatField(null=False)
	quantity = models.PositiveIntegerField(null=False)
	datetime = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.trade_id


class AppleFirmOrder(models.Model):
	trade_id = models.PositiveIntegerField(primary_key=True, null=False)
	customer_id = models.PositiveIntegerField()
	trade_type = models.CharField(max_length=200, null=False)
	security_type = models.CharField(max_length=200, null=False)
	security_name = models.CharField(max_length=200, null=False)
	price = models.FloatField(null=False)
	quantity = models.PositiveIntegerField(null=False)
	datetime = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.trade_id


class FacebookCustomerOrder(models.Model):
	trade_id = models.PositiveIntegerField(primary_key=True, null=False)
	customer_id = models.PositiveIntegerField()
	trade_type = models.CharField(max_length=200, null=False)
	security_type = models.CharField(max_length=200, null=False)
	security_name = models.CharField(max_length=200, null=False)
	price = models.FloatField(null=False)
	quantity = models.PositiveIntegerField(null=False)
	datetime = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.trade_id

class FacebookFirmOrder(models.Model):
	trade_id = models.PositiveIntegerField(primary_key=True, null=False)
	customer_id = models.PositiveIntegerField()
	trade_type = models.CharField(max_length=200, null=False)
	security_type = models.CharField(max_length=200, null=False)
	security_name = models.CharField(max_length=200, null=False)
	price = models.FloatField(null=False)
	quantity = models.PositiveIntegerField(null=False)
	datetime = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.trade_id

class WallmartCustomerOrder(models.Model):
	trade_id = models.PositiveIntegerField(primary_key=True, null=False)
	customer_id = models.PositiveIntegerField()
	trade_type = models.CharField(max_length=200, null=False)
	security_type = models.CharField(max_length=200, null=False)
	security_name = models.CharField(max_length=200, null=False)
	price = models.FloatField(null=False)
	quantity = models.PositiveIntegerField(null=False)
	datetime = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.trade_id

class WalmartFirmOrder(models.Model):
	trade_id = models.PositiveIntegerField(primary_key=True, null=False)
	customer_id = models.PositiveIntegerField()
	trade_type = models.CharField(max_length=200, null=False)
	security_type = models.CharField(max_length=200, null=False)
	security_name = models.CharField(max_length=200, null=False)
	price = models.FloatField(null=False)
	quantity = models.PositiveIntegerField(null=False)
	datetime = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.trade_id