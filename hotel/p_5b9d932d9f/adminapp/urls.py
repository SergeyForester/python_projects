app_name = 'adminapp'

from django.urls import path
import adminapp.views as adminapp

urlpatterns = [
    path('', adminapp.mainAdminPage, name='main'),
    path('create/', adminapp.createARoom, name='create'),
    path('view/', adminapp.viewAllRooms, name='view'),
    path('edit/room-<int:pk>/', adminapp.editRoom, name='edit'),
    path('book/', adminapp.bookARoom, name='book'),

]