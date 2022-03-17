from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns = [
    path('', views.ReservationList.as_view(), name='main'),
    path('create/', views.reservation_create, name='reservation_create'),
    path('edit/<int:pk>/', views.reservation_edit, name='reservation_edit'),
    path('delete/<int:pk>/', views.reservation_delete, name='reservation_delete'),

]
