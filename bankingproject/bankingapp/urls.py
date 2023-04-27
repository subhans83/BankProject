from django.urls import path
from . import views
from users import views as user_views
app_name = 'bankingapp'
urlpatterns = [
    path('', views.index, name='index'),


    path('register_success/', views.register_success, name='register_success'),
    path('member/add/', views.create_view, name='add'),

    path('member/ajax/load-branches/', views.load_branches, name='ajax_load_branches'),  # AJAX
    path('user_created/',views.user_created,name='user_created'),

]
