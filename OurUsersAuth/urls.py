from django.urls import path
from OurUsersAuth import views

urlpatterns = [
    path('login-email-auth', views.loginTheUserviaEmail, name='loginTheUserEmail'),
    path('login-username-auth', views.loginTheUserviaUsername, name='loginTheUserUsername'),
    path('signup/', views.signup, name='signup'),
    path('forget-password-identification/', views.ForgetPassword, name='forget-password'),
    path('set-new-password', views.SetNewPassword, name='SetNewPassword'),
    path('myProfile/', views.Profile, name='myProfile'),
    path('logout/', views.logoutTheUser, name='logoutTheUser'),
]