from django.contrib          import admin
from django.urls             import path,include
from django.conf             import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',      admin.site.urls ),
    path('projects/',   include('projects.urls') ),
    path('profile/',    include('users.urls') ),

] + static( settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )

admin.site.site_header = 'Portfolio Site' 
admin.site.index_title = 'Models Of Site'                 
admin.site.site_title  = 'Administration'


