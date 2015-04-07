from .models import Principal
from rest_framework import serializers


class PrincipalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Principal
        fields = ('Namelg_principal', 'federationorg_principal', 'countryorg_principal', 'startdate_principal', 'enddate_principal', 'qteams_principal', 'leagueformat_principal',)
