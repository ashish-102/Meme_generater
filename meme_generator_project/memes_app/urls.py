from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.user_login, name='signin'),
    path('registration/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('editor-page/', views.editor_home, name='editor'),
    path('meme-download-page/', views.meme_download, name='downloader'),
    path('meme-delete/<int:pk>', views.del_meme, name='delete'),
]
