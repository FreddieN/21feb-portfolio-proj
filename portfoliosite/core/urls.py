from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<str:project_id>', views.project_view.as_view(), name="project_view"),
] 