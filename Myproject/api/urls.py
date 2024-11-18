from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes),
    # path('rooms/',views.getRooms),
    path('messages/',views.getMessages),
    path('messages/<str:id>/',views.getMessage),
]