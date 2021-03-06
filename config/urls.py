from django.contrib import admin
from django.urls import include, path
from config import views


urlpatterns = [
    path('health/', views.health),
    path('recommend/', include('apps.recommend.urls')),
    path('admin/', admin.site.urls),
]
