from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('', views.frontpage, name="fontpage"),
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name="chat_app/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),

    # request
    path('friendRequest/<slug:slug>', views.friendRequest, name="friendRequest"),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)