from django.db import models

# datovy model konsolidovanych udajov


class Esu2010Code(models.Model):
	name = models.CharField(max_length=128)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'esu2010_codes'


class MainActivityCode(models.Model):
	name = models.CharField(max_length=128)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'main_activity_codes'



class Organization(models.Model):
	established_on = models.DateField()
	terminated_on = models.DateField(null=True)
	esu2010_code = models.ForeignKey(Esu2010Code, on_delete=models.DO_NOTHING)
	main_activity_code = models.ForeignKey(MainActivityCode, on_delete=models.DO_NOTHING)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'organizations'


class OrganizationIdentifier(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	ipo = models.IntegerField()
	effective_from = models.DateField()
	effective_to = models.DateField(null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	class Meta():
		db_table = 'organization_identifier_entries'


class OrganizationName(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	name = models.CharField(max_length=512)
	effective_from = models.DateField()
	effective_to = models.DateField(null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'organization_name_entries'


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
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'organization_address_entries'

class LegalForms(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	name = models.CharField(max_length=128)
	effective_from = models.DateField()
	effective_to = models.DateField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'organization_legal_forms'

class OrganizationLegalForms(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	legal_form_id = models.ForeignKey(LegalForms, null=True, on_delete=models.DO_NOTHING)
	effective_from = models.DateField()
	effective_to = models.DateField(null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'organization_legal_forms_entries'

class OrganizationLegalStatus(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	body = models.CharField(max_length=128)
	effective_from = models.DateField()
	effective_to = models.DateField(null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'organization_legal_status_entries'

class MainActivityCodes:
	name = models.CharField()

	class Meta():
		db_table = 'main_activity_codes'

class OrganizationEconomicActivity(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	description = models.CharField(max_length=128)
	effective_from = models.DateField()
	effective_to = models.DateField(null=True)
	suspended_from = models.DateField(null=True)
	suspended_to = models.DateField(null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'organization_economic_activity'

class StakeholderTypes(models.Model):
	name = models.CharField(max_length=128)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'stakeholder_types'

class OrganizationStatutoryEntries(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	stakeholder_type = models.ForeignKey(StakeholderTypes,null=True,  on_delete=models.DO_NOTHING)
	full_name = models.CharField(null=True, max_length=128)
	person_given_name = models.CharField(null=True, max_length=128)
	person_family_name = models.CharField(null=True, max_length=128)
	person_given_family_name = models.CharField(null=True, max_length=128)
	person_prefixes = models.CharField(null=True, max_length=128)
	person_postfixes = models.CharField(null=True, max_length=128)
	address_formatted = models.CharField(null=True, max_length=128)
	address_street = models.CharField(null=True, max_length=128)
	address_reg_number = models.IntegerField(null=True)
	address_building_number = models.CharField(null=True, max_length=128)
	address_postal_code = models.CharField(null=True, max_length=128)
	address_municipality = models.CharField(null=True, max_length=128)
	address_country = models.CharField(null=True, max_length=128)
	effective_from = models.DateField()
	effective_to = models.DateField(null=True)
	ico = models.IntegerField(null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'organization_statutory_entries'

class OrganizationStakeholderEntries(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	stakeholder_type = models.ForeignKey(StakeholderTypes, on_delete=models.DO_NOTHING)
	full_name = models.CharField(null=True, max_length=256)
	person_given_name = models.CharField(null=True, max_length=51)
	person_family_name = models.CharField(null=True, max_length=51)
	person_given_family_name = models.CharField(null=True, max_length=26)
	person_prefixes = models.CharField(null=True, max_length=17)
	person_postfixes = models.CharField(null=True, max_length=10)
	address_formatted = models.CharField(null=True, max_length=176)
	address_street = models.CharField(null=True, max_length=128)
	address_reg_number = models.IntegerField()
	address_building_number = models.CharField(null=True, max_length=21)
	address_postal_code = models.CharField(null=True, max_length=11)
	address_municipality = models.CharField(null=True, max_length=128)
	address_country = models.CharField(null=True, max_length=128)
	address_effective_from = models.DateField(null=True)
	address_effective_to = models.DateField(null=True)
	address_effective_to
	effective_from = models.DateField()
	effective_to = models.DateField(null=True)
	ico = models.IntegerField(null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'organization_stakeholder_entries'

class OrganizationDepositEntries(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	full_name = models.CharField(null=True, max_length=256)
	person_given_name = models.CharField(null=True, max_length=51)
	person_family_name = models.CharField(null=True, max_length=51)
	person_given_family_name = models.CharField(null=True, max_length=26)
	person_prefixes = models.CharField(null=True, max_length=17)
	person_postfixes = models.CharField(null=True, max_length=10)
	deposit_amount = models.DecimalField(max_digits=13, decimal_places=2)
	deposit_currency = models.CharField(max_length=9)
	deposit_type = models.CharField(max_length=256)
	effective_from = models.DateField()
	effective_to = models.DateField(null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'organization_deposit_entries'


class OrganizationOtherLegalFact(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	body = models.TextField()
	effective_from = models.DateField()
	effective_to = models.DateField(null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'organization_other_legal_fact_entries'


class ShareForm(models.Model):
	name = models.CharField(max_length=24)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'share_forms'


class ShareType(models.Model):
	name = models.CharField(max_length=24)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
		
	class Meta():
		db_table = 'share_types'


class OrganizationShare(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	share_type = models.ForeignKey(ShareType, on_delete=models.DO_NOTHING)
	share_form = models.ForeignKey(ShareForm, null=True, on_delete=models.DO_NOTHING)
	share_price = models.DecimalField(max_digits=13, decimal_places=2)
	share_currency = models.CharField(max_length=8)
	share_amount = models.BigIntegerField()
	share_transfer = models.TextField(null=True)
	effective_from = models.DateField()
	effective_to = models.DateField(null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'organization_share_entries'
	

#  ======= RKUV =======

class EndUser(models.Model):
	name = models.CharField(max_length=64)
	address = models.CharField(max_length=128)
	identification = models.CharField(max_length=48)
	public_official = models.BooleanField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'end_users'
			

class OrganizationEndUser(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	end_user = models.ForeignKey(EndUser, on_delete=models.DO_NOTHING)
	valid_since = models.DateField()
	last_change = models.DateField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'organization_end_user_entries'


#  ======= otvoreneZmluvy =======

class CustomerRecord(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	qtr_year = models.IntegerField()
	year = models.IntegerField()
	sum_money = models.DecimalField(max_digits=13, decimal_places=2)
	sum_contracts = models.IntegerField()
	url = models.URLField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'customer_records'


class SupplierRecord(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	qtr_year = models.IntegerField()
	year = models.IntegerField()
	sum_money = models.DecimalField(max_digits=13, decimal_places=2)
	sum_contracts = models.IntegerField()
	url = models.URLField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'supplier_records'

#  ======= otvoreneSudy =======

class AdjudgementRecord(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
	qtr_year = models.IntegerField()
	year = models.IntegerField()
	records_count = models.IntegerField()
	url = models.URLField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'adjudgement_records'


class LegislationSubarea(models.Model):
	name = models.CharField(unique=True, max_length=128)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'legislation_subareas'


class AdjudgementRecordLegislationSubarea(models.Model):
	adjudgement_record = models.ForeignKey(AdjudgementRecord, on_delete=models.DO_NOTHING)
	legislation_subarea = models.ForeignKey(LegislationSubarea, on_delete=models.DO_NOTHING)
	records_count = models.SmallIntegerField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'adjudgement_record_legislation_subarea_entries'


class AdjudgementNature(models.Model):
	name = models.CharField(unique=True, max_length=128)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'adjudgement_natures'


class AdjudgementRecordAdjudgementNature(models.Model):
	adjudgement_record = models.ForeignKey(AdjudgementRecord, on_delete=models.DO_NOTHING)
	adjudgement_nature = models.ForeignKey(AdjudgementNature, on_delete=models.DO_NOTHING)
	records_count = models.SmallIntegerField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta():
		db_table = 'adjudgement_record_adjudgement_nature_entries'