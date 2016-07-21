from django.db import models


class BenefitEndUser(models.Model):
	valid_since = models.DateField();
	last_change = models.DateField();
	name = models.CharField(max_length=64);
	address = models.CharField(max_length=128);
	identification = models.CharField(max_length=48);
	public_official = models.BooleanField();
