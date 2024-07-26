from django.urls import path

from . import views

urlpatterns = [
    path('create_newpost/', views.create_newpost, name='create_newpost'),
    path('delete_post/', views.delete_post, name='delete_post'),
    path('confirm_delete_post/<post_id>', views.confirm_delete_post, name='confirm_delete_post'),
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:slug>', views.detail, name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail')
]