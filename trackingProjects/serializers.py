from rest_framework import serializers
from .models import Dossier

class DossierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dossier
        fields = ['Nom','Prenom','Cin','status']
        