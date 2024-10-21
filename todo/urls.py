from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index,name='index'),
    path('', views.home),
    path('signup/', views.signup),
    path('loginn/', views.loginn),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('update/<str:pk>', views.update, name='update'),
    path('remove_all/', views.remove_all, name='remove_all'),
    path('signout/', views.signout, name='signout'),
]