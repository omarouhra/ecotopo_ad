from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Dossier

from rest_framework import filters, generics


from .serializers import DossierSerializer

# Create your views here.
 
    
class Search(generics.ListAPIView):
    queryset = Dossier.objects.all()
    serializer_class = DossierSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=Cin']





    


    