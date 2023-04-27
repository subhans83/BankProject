from . import views
from django.urls import path

from users import views as user_views
app_name="users"
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='login'),
    path('signout/', views.signout, name='logout'),
    path('register',views.register,name='register')

]
