"""
URL configuration for liquiseife_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('api_app.urls')),
]

# In our settings.py we specified in our MEDIA_URL variable the url pattern we would want to locate our uploaded static files and we specified in our MEDIA_ROOT variable, the directory that our uploaded files to django should be saved to
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
print(f"The url patterns: {urlpatterns}")