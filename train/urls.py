
from django.urls import path
from train.views import *
urlpatterns = [
    path('login/',login_page,name="login"),
    path("logout_page/",logout_page,name='loguot'),
   path('delete_page/<id>/',delete_page,name="deletepage"),
    path('update_page/<id>/',update_page,name="updatepage"),
    path('register/',register,name="register"),
    path('page/',page,name="page"),
    
]
