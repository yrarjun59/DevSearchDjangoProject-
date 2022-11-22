from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls')),
    path('projects/',include('projects.urls')),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='reset_password'),
  
    path('password-reset-instruction-sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),name='password_reset_done'),
  
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
  
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)