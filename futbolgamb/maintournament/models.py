from django.db import models

# Create your models here.


class Principal(models.Model):
	id = models.AutoField(primary_key=True)
	Namelg_principal = models.CharField(max_length=255)
	federationorg_principal = models.CharField(max_length=20)
	countryorg_principal = models.CharField(max_length=20)
	startdate_principal = models.DateField()
	enddate_principal = models.DateField()
	qteams_principal = models.IntegerField()
	leagueformat_principal = models.IntegerField()

	def __unicode__(self):
		return self.Namelg_principal