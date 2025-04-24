"""
URL configuration for bookstore project.

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
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

#Written by Noe 
from core.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls")),
    path("user/", include("userauths.urls")),
    path("vendoradmin/", include("vendoradmin.urls")),

    path("ckeditor5/", include('django_ckeditor_5.urls')),
]


# Always serve media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Static files only needed with DEBUG=True since we're using whitenoise in production
if settings.DEBUG:
    # All the static files are stored in the roots directory in a folder called static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
