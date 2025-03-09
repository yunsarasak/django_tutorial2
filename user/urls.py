from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns=[
    # path('login/', views.load_user_login, name='load_user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('login/', views.user_login, name='user_login'),
]

# urlpatterns=[
#     path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
# ]