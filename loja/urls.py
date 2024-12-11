from django.contrib import admin
from django.urls import path, include  
from gerenciamento import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base, name='base'),  
    path('gerenciamento/', include('gerenciamento.urls')),  
]
