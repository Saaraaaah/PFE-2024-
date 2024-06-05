from django.urls import path
from . import views
from .views import generate_map_view

urlpatterns = [
   # path('', views.index, name='index'),
   path('per/',views.user_perm,name='per'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    #path('main-map/',views.main_map,name='main-map'),
    path('', views.carte, name='carte'),
    # path('get-less-rout/',views.get_less_rout,name='get-less-rout'),
    path('generate-and-download-image/',views.generate_image_and_save,name='generate-and-download-image'),
    path('logout/',views.LogoutPage,name='logout'),
  #  path('signup/',views.testfunc,name='signup'),
    
    path('responsable/',views.respo,name='responsable'),
    path('citoyen/', generate_map_view, name='generate_map'),

   # path('generate_map/', views.generate_map_with_user_and_posta, name='generate_map'),
]
