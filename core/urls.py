from django.urls import path
from . import views,auth_views
urlpatterns = [
    path('', views.index, name='home'),
    path("filterauthor/", views.filter_author, name="filter_author"),
    path('addpost/', views.create_post, name='add_post'),
    path('login/', auth_views.loginn, name='login'),
    path('register/', auth_views.register, name='register'),
    path('logout',auth_views.logoutt, name='logout')
]