from django.urls import path
import views

urlpatterns = [
    path('', views.getUser),
    path('create', views.addUser),
    path('read/<str: id>', views.getUserById),
    path('update/<str: id>', views.updateUser),
    path('delete/<str: id>', views.deleteUser)
]
