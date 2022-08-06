from django.contrib.auth import views as auth_views
from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('', views.rooms, name="rooms"),
    path('<slug:slug>/', views.room, name="room"),
    
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)