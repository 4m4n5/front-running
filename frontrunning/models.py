import datetime

from django.db import models
from django.utils import timezone
# Create your models here.
class AppleOrder(models.Model):
	trade_id = models.PositiveIntegerField(primary_key=True, null=False)
	customer_id = models.PositiveIntegerField()
	trade_type = models.CharField(max_length=200, null=False)
	security_type = models.CharField(max_length=200, null=False)
	security_name = models.CharField(max_length=200, null=False)
	price = models.FloatField(null=False)
	quantity = models.PositiveIntegerField(null=False)
	datetime = models.DateTimeField(auto_now=True)
	def __str__(self):
		return str(self.trade_id)


class FacebookOrder(models.Model):
	trade_id = models.PositiveIntegerField(primary_key=True, null=False)
	customer_id = models.PositiveIntegerField()
	trade_type = models.CharField(max_length=200, null=False)
	security_type = models.CharField(max_length=200, null=False)
	security_name = models.CharField(max_length=200, null=False)
	price = models.FloatField(null=False)
	quantity = models.PositiveIntegerField(null=False)
	datetime = models.DateTimeField(auto_now=True)
	def __str__(self):
		return str(self.trade_id)

class WalmartOrder(models.Model):
	trade_id = models.PositiveIntegerField(primary_key=True, null=False)
	customer_id = models.PositiveIntegerField()
	trade_type = models.CharField(max_length=200, null=False)
	security_type = models.CharField(max_length=200, null=False)
	security_name = models.CharField(max_length=200, null=False)
	price = models.FloatField(null=False)
	quantity = models.PositiveIntegerField(null=False)
	datetime = models.DateTimeField(auto_now=True)
	def __str__(self):
		return str(self.trade_id)