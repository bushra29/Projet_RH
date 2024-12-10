"""
URL configuration for projetRH project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from demandes import views
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from demandes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forms/', include('demandes.urls', namespace='demandes')),
    path('', views.home, name='home'),
]

# Ajoutez les URL pour servir les fichiers médias et statiques en mode DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # Ajoutez le panneau de débogage si DEBUG est activé
    # import debug_toolbar
    # urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

