from django.urls import path
from .views import Search
urlpatterns = [
    
    path('Search/', Search.as_view(), name="Search"),
   

]