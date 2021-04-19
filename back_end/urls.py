from django.contrib import admin
from django.urls import path
from trackingProjects.views import Search


urlpatterns = [
    path('', Search.as_view() , name="Search"),
    path('admin/', admin.site.urls),



]
