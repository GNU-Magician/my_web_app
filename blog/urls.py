from django.urls import path

from . import views

urlpatterns = [
    path('blog/', views.IndexView.as_view(), name='index')
]