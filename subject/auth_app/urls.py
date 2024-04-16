from django.urls import path
from .views import user_login, user_signup, user_logout, change_password


urlpatterns = [
    path('login/', user_login, name='login_url'),
    path('signup/', user_signup, name='signup_url'),
    path('logout/', user_logout, name='logout_url'),
    path('cpass/', change_password, name='cpass_url'),
]
