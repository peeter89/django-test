from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
# Use include() to add URLS from the catalog application and authentication system


urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

urlpatterns += [
    path('clown/', include('clown.urls')),
]

# Use static() to add url mapping to serve static files during development (only)

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Add URL maps to redirect the base URL to our application

urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
