from django.urls import include, path
from apps.recommend import views

app_name = 'recommend'

urlpatterns = [
    path('<int:pk>/', views.Recommend.as_view(), name='recommend'),
    path('<int:pk>/no-lti/', views.RecommendTest.as_view()),
    path('<int:pk>/ui-test/', views.RecommendUITest.as_view()),
]
