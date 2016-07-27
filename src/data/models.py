from django.db import models

# datovy model konsolidovanych udajov


class Organization(models.Model):


	class Meta():
		db_table = 'organization'


class OrganizationIdentifier(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	ipo = models.IntegerField()
	effective_from = models.DateField()
	effective_to = models.DateField(null=True)
	
	class Meta():
		db_table = 'organization_identifier'


class OrganizationName(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	name = models.CharField(max_length=512)
	effective_from = models.DateField()
	effective_to = models.DateField(null=True)

	class Meta(models.Model):
			db_table = 'organization_name'


class OrganizationAddress(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	formatted_address = models.CharField(max_length=256)
	street = models.CharField(max_length=128)
	reg_number = models.IntegerField()
	building_number = models.CharField(max_length=128)
	postal_code = models.CharField(max_length=16)
	municipality = models.CharField(max_length=128)
	country = models.CharField(max_length=64)
	effective_from = models.DateField()
	effective_to = models.DateField(null=True)

	class Meta(models.Model):
			db_table = 'organization_address'

					
#  ======= RKUV =======

class EndUser(models.Model):
	name = models.CharField(max_length=64)
	address = models.CharField(max_length=128)
	identification = models.CharField(max_length=48)
	public_official = models.BooleanField()

	class Meta():
		db_table = 'end_user'
			

class Organization_EndUser(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	end_user = models.ForeignKey(EndUser, on_delete=models.DO_NOTHING)
	valid_since = models.DateField()
	last_change = models.DateField()

	class Meta():
		db_table = 'organization_end_user'


#  ======= otvoreneZmluvy =======

class Customer(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	qtr_year = models.IntegerField()
	year = models.IntegerField()
	sum_money = models.DecimalField(max_digits=13, decimal_places=2)
	sum_contracts = models.IntegerField()
	url = models.URLField()

	class Meta():
		db_table = 'customer'


class Supplier(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	qtr_year = models.IntegerField()
	year = models.IntegerField()
	sum_money = models.DecimalField(max_digits=13, decimal_places=2)
	sum_contracts = models.IntegerField()
	url = models.URLField()

	class Meta():
		db_table = 'supplier'

#  ======= otvoreneSudy =======

class AdjudgementRecord(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	qtr_year = models.IntegerField()
	year = models.IntegerField()
	records_count = models.IntegerField()
	url = models.URLField()

	class Meta():
		db_table = 'adjudgement_record'


class LegislationSubarea(models.Model):
	name = models.CharField(unique=True, max_length=128)

	class Meta():
		db_table = 'adjudgement_legislation_subarea'


class AdjudgementRecord_LegislationSubarea(models.Model):
	adjudgement_record = models.ForeignKey(AdjudgementRecord, on_delete=models.DO_NOTHING)
	legislation_subarea = models.ForeignKey(LegislationSubarea, on_delete=models.DO_NOTHING)
	records_count = models.SmallIntegerField()

	class Meta():
		db_table = 'adjudgement_record_legislation_subarea'


class AdjudgementNature(models.Model):
	name = models.CharField(unique=True, max_length=128)

	class Meta():
		db_table = 'adjudgement_nature'


class AdjudgementRecord_AdjudgementNature(models.Model):
	adjudgement_record = models.ForeignKey(AdjudgementRecord, on_delete=models.DO_NOTHING)
	adjudgement_nature = models.ForeignKey(AdjudgementNature, on_delete=models.DO_NOTHING)
	records_count = models.SmallIntegerField()

	class Meta():
		db_table = 'adjudgement_record_adjudgement_nature'