from .models import PhaseA
from rest_framework import serializers


class PhaseASerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PhaseA
        fields = ('idleague_fasea', 'group_fasea', 'idmatch_fasea', 'idteamlg_fasea', 'nameteam_fasea', 'goals_fasea', 'points_fasea',)