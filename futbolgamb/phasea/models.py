from django.db import models

# Create your models here.

class PhaseA(models.Model):
	id = models.AutoField(primary_key=True)
	idleague_fasea = models.IntegerField()
	group_fasea = models.CharField(max_length=2)
	idmatch_fasea = models.IntegerField()
	idteamlg_fasea = models.IntegerField()
	nameteam_fasea = models.CharField(max_length=20)
	goals_fasea = models.IntegerField()
	points_fasea = models.IntegerField()	

	def __unicode__(self):
		return self.nameteam_fasea