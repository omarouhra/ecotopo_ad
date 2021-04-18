from django.contrib import admin
from .models import Dossier

# Register your models here.
class DossierAdmin(admin.ModelAdmin):
    list_display = ['Nom', 'Prenom', 'Cin', 'Rf','Prestation', 'status', 'created_at']
    list_filter = ['status','Prestation','created_at']
    search_fields =['Cin','Nom']
    
admin.site.register(Dossier,DossierAdmin)