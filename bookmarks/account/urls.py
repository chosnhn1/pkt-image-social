from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # path('login/', views.user_login, name='login' ),

    # Using django's view
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password-change/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # path('pawword-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('pawword-reset/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_reset_done'),
    # path('pawword-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('pawword-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Using contrib.auth.urls views for auth
    path('', include('django.contrib.auth.urls')),
    
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]

# Media file service location while DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)