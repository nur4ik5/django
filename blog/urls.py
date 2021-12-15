from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name = "index"),

    path('user_list/', views.user_list, name = "user_list"),

    path('message/', views.message, name = 'message'),

    path('login/', views.login, name = 'login'),

    ####################### Posts ################################
    path('posts/', views.posts_list, name = 'posts_list'),

    path('posts/<pk>', views.post_detail, name = 'post_detail'),

    path('posts/create', views.post_create, name = 'post_create'),

    ###################### ADV #################################

    path('advertisement/', views.advertisement, name = 'advertisement'),

    path('advertisement/<adv_id>/delete', views.advertisement_delete, name = 'advertisement_delete'),
]
