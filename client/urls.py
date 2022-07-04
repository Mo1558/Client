from django import views
from django.urls import path
from .  import views

app_name='client'
urlpatterns = [
    path('clients/',views.display_clients,name='All_Clients'),             #url to display all clients  
    path('clients/add/',views.add_client,name='Add_Client'),                   #url to add client
    path('clients/<int:id>/',views.display_client,name='Display_Client'),   #url to display specific client
    path('clients/<int:id>/update/',views.update_client,name='Update_Client'),    #url to update specific client
    path('clients/<int:id>/delete/',views.delete_client,name='Delete_Client'),    #url to delete specific client
]