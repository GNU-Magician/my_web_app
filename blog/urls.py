from django.urls import path

from . import views
app_name = 'blog'
urlpatterns = [
    path('blog/', views.IndexView.as_view(), name='index'),
    # ex: /blog

    path('blog/create', views.create_post, name='create_post'),
    #ex: /blog/create

    path('blog/delete/<int:pk>', views.DeletePost.as_view(), name='delete_post'),

    path('account/register', views.register, name='register')

]