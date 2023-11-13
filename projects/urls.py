from django.urls             import path
from .views                  import ProjectListView, ProjectDetailView, MineProjectListView, MineProjectDetailView

urlpatterns = [

    # PROJECT-URLS.PY

    # FOR ME
    path('',          MineProjectListView.as_view(),   name='mine_project_list'),
    path('<int:pk>/', MineProjectDetailView.as_view(), name='mine_project_detail'),

    # FOR USERS
    path('<str:username>/',          ProjectListView.as_view(),   name='project_list'),
    path('<str:username>/<int:pk>/', ProjectDetailView.as_view(), name='project_detail')
] 
