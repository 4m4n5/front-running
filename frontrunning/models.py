from django.db import models

# Create your models here.
class AppleCustomerOrder(models.Model):
	trade_id = models.PositiveIntegerField(primary_key=True, null=False)
	customer_id = models.PositiveIntegerField()
	trade_type = models.models.CharField(max_length=200, null=False)
	security_type = models.CharField(max_length=200, null=False)
	security_name = models.CharField(max_length=200, null=False)
	price = models.FloatField(null=False)
	quantity = models.PositiveIntegerField(null=False)
	datetime = models.DateTimeField(auto_now=True)


class AppleFirmOrder(models.Model):
	trade_id = models.PositiveIntegerField(primary_key=True, null=False)
	customer_id = models.PositiveIntegerField()
	trade_type = models.models.CharField(max_length=200, null=False)
	security_type = models.CharField(max_length=200, null=False)
	security_name = models.CharField(max_length=200, null=False)
	price = models.FloatField(null=False)
	quantity = models.PositiveIntegerField(null=False)
	datetime = models.DateTimeField(auto_now=True)


class FacebookCustomerOrder(models.Model):
	trade_id = models.PositiveIntegerField(primary_key=True, null=False)
	customer_id = models.PositiveIntegerField()
	trade_type = models.models.CharField(max_length=200, null=False)
	security_type = models.CharField(max_length=200, null=False)
	security_name = models.CharField(max_length=200, null=False)
	price = models.FloatField(null=False)
	quantity = models.PositiveIntegerField(null=False)
	datetime = models.DateTimeField(auto_now=True)

class FacebookFirmOrder(models.Model):
	trade_id = models.PositiveIntegerField(primary_key=True, null=False)
	customer_id = models.PositiveIntegerField()
	trade_type = models.models.CharField(max_length=200, null=False)
	security_type = models.CharField(max_length=200, null=False)
	security_name = models.CharField(max_length=200, null=False)
	price = models.FloatField(null=False)
	quantity = models.PositiveIntegerField(null=False)
	datetime = models.DateTimeField(auto_now=True)

class WallmartCustomerOrder(models.Model):
	trade_id = models.PositiveIntegerField(primary_key=True, null=False)
	customer_id = models.PositiveIntegerField()
	trade_type = models.models.CharField(max_length=200, null=False)
	security_type = models.CharField(max_length=200, null=False)
	security_name = models.CharField(max_length=200, null=False)
	price = models.FloatField(null=False)
	quantity = models.PositiveIntegerField(null=False)
	datetime = models.DateTimeField(auto_now=True)

class WalmartFirmOrder(models.Model):
	trade_id = models.PositiveIntegerField(primary_key=True, null=False)
	customer_id = models.PositiveIntegerField()
	trade_type = models.models.CharField(max_length=200, null=False)
	security_type = models.CharField(max_length=200, null=False)
	security_name = models.CharField(max_length=200, null=False)
	price = models.FloatField(null=False)
	quantity = models.PositiveIntegerField(null=False)
	datetime = models.DateTimeField(auto_now=True)