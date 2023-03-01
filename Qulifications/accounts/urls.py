from django.urls import path
from . import views
app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup,name='signup_page'),
    path('logoin/', views.login_user,name='login_page'),
    path('logout/', views.logout_user,name='logout_page'),
]

