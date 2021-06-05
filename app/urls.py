from django.urls import path
from . import views

urlpatterns = [
    path("createview",views.create_view,name="createview"),
    path("list_view",views.list_view,name="list_view"),
    path('<id>', views.detail_view ),
    path('<id>/delete', views.delete_view ),
    path('<id>/update', views.update_view ),
    
    
    

]
