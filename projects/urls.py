from django.urls             import path
from .views                  import ProjectListView,ProjectDetailView

urlpatterns = [
    path('<str:username>/',          ProjectListView.as_view(),   name='project_list'),
    path('<str:username>/<int:pk>/', ProjectDetailView.as_view(), name='project_detail')
] 
