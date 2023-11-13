from django.urls             import path
from .views                  import ProfileView, MineProfileView

urlpatterns = [

    # USERS-URLS.PY

    # FOR ME
    path('',  MineProfileView.as_view(),   name='mine_profile_detail'),

    # FOR USERS
    path('<str:username>/',  ProfileView.as_view(),   name='profile_detail'),
] 
