from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:id>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:id>/delete/', views.post_delete, name='post_delete'),
    path('signup/', views.signup, name='signup'), 
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('account/delete/', views.delete_account, name='delete_account'),
    path('account/settings/', views.account_settings, name='account_settings'),
    path('category/<int:category_id>/', views.post_list, name='category_posts'),
]
