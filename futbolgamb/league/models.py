from django.db import models

# Create your models here.

class League(models.Model):
    id=models.AutoField(primary_key=True)
    id_League = models.IntegerField(max_length=255)
    group_League= models.CharField(max_length=255)
    idteam_League= models.IntegerField(max_length=255)
    nameteam_League= models.CharField(max_length=255)
    team_League= models.CharField(max_length=255)
    matches_league= models.IntegerField(max_length=255)
    wins_league= models.IntegerField(max_length=255)
    matched_league= models.IntegerField(max_length=255)
    lose_league= models.IntegerField(max_length=255)
    points_league= models.IntegerField(max_length=255)
    position_league= models.IntegerField(max_length=255)    

    def __unicode__(self):
        return self.nameteam_League