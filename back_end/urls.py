from django.contrib import admin
from django.urls import path
from trackingProjects.views import Search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Search/', Search.as_view() , name="Search"),



]
