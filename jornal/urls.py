from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # 👈 ESTA LINHA É A CHAVE
    path('', include('noticias.urls')),
]
