from django.urls import path
from . import views


urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('films/addFilm', views.AddFilm.as_view(), name= 'add_film'),
    path('films/addDirector', views.AddDirector.as_view(), name= 'add_film'),
    path('films/update/<slug:pk>', views.UpdateFilm.as_view(), name= 'update_film')
]