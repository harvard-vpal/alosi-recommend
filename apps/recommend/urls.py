from django.urls import include, path
from apps.recommend import views

app_name = 'recommend'

urlpatterns = [
    path('<slug:collection_id>/', views.Recommend.as_view(), name='recommend'),
    path('<slug:collection_id>/no-lti/', views.RecommendTest.as_view()),
    path('<slug:collection_id>/ui-test/', views.RecommendUITest.as_view()),
]

