from django.urls import path
from social_django.urls import urlpatterns as social_django_urlpatterns
from .views import LogoutView, LogInView

app_name = 'accounts'

urlpatterns = [
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]

urlpatterns += social_django_urlpatterns

