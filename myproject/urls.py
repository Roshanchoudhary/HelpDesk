from django.contrib import admin
from django.urls import path
from . import views  # Naya import

urlpatterns = [
    path('', views.set_password, name='set_password'), # Home page par ye chalega
    path('admin/', admin.site.urls),
]
