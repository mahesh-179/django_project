from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="home"),
    path('records/', views.home, name="home"),  # recorded data page
     path('admin/', views.admin, name="admin"),  # recorded data page

]
