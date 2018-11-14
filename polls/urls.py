from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /polls/create/
    path('create/', views.createPage, name='create_page'),
    # ex: /polls/create/object/
    path('create/object', views.create, name='create'),
    # ex: /polls/create/choice/
    path('create/choice', views.CreateChoicePage.as_view(), name='create_choice_page'),
    # ex: /polls/What's going on/create
    path('delete/<int:pk>/', views.deleteView.as_view(), name='delete_question'),
    # ex: polls/delete/32

    path('create/choice/<int:pk>', views.create_choice, name='create_choice'),

    path('gg', views.newIndex, name='dashboard_index'),

]