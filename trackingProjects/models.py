from django.db import models

# Create your models here.

class Dossier(models.Model):
    # status
    LEVE = 'levé'
    TRAITEMENT = 'traitement'
    COMPLETED = 'completed'
    CONTROLEAUCADASTRE = 'controle de cadastre'
    RECEPESEDELEVRE = 'recepese delivré'
    STATUS_CHOICES = (
        (LEVE,'levé'),
        (TRAITEMENT,'traitement'),
        (CONTROLEAUCADASTRE,'controle de cadastre'),
        (RECEPESEDELEVRE, 'recepese delivré'),
    )
    # prestations
    MEC = 'M.E.C'
    MT = 'MT'
    LOTISSEMENT = 'lotissement'
    MTFUSION = 'MT Fustion'
    FUSIONTOTAL = 'Fusion total'
    COPROPRIETE = 'copropriété'
    PLANDEBORNAGE = ' Plan de bornage'
    PLANCOTE = 'Plan cote'
    PARTAGE = 'Partage'
    EXPERTISEFONCIER = 'Expertise foncier'
    PRESTATION_CHOICES = (
        (MEC, 'M.E.T'),
        (MT,'MT'),
        (LOTISSEMENT,'Lotissement'),
        (MTFUSION, 'MT Fustion'),
        (FUSIONTOTAL, 'Fusion total'),
        (COPROPRIETE , 'Copropriété'),
        (PLANDEBORNAGE, ' Plan de bornage'),
        (PLANCOTE, 'Plan cote'),
        (PARTAGE, 'Partage'),
        (EXPERTISEFONCIER, 'Expertise foncier'),
    )
   
    Nom = models.CharField( max_length=100)
    Prenom = models.CharField( max_length=100)
    Cin = models.CharField( max_length=100)
    Rf = models.CharField( max_length=100)
    Prestation = models.CharField( max_length=100,choices=PRESTATION_CHOICES,blank=True)
    Lieu = models.CharField( max_length=100)
    status = models.CharField( max_length=100,choices=STATUS_CHOICES,default='confirmed',)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)