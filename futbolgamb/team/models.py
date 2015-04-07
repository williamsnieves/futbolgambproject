from django.db import models

# Create your models here.

class Team(models.Model):
    id=models.AutoField(primary_key=True)
    name_team = models.CharField(max_length=255)
    id_team= models.CharField(max_length=255)
    fed_team= models.CharField(max_length=255)
    country_team= models.CharField(max_length=255)   

    def __unicode__(self):
        return self.name_team