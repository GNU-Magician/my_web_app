from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('polls/', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('polls/<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('polls/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /polls/create/
    path('polls/create/', views.createPage, name='create_page'),
    # ex: /polls/create/object/
    path('polls/create/object', views.create, name='create'),
    # ex: /polls/create/choice/
    path('polls/create/choice', views.CreateChoicePage.as_view(), name='create_choice_page'),
    # ex: /polls/What's going on/create
    path('polls/delete/<int:pk>/', views.deleteView.as_view(), name='delete_question'),
    # ex: polls/delete/32

    path('polls/create/choice/<int:pk>', views.create_choice, name='create_choice'),

    path('', views.newIndex, name='dashboard_index'),

]