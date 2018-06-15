from django.urls import include, path
from apps.recommend import views

app_name = 'recommend'

urlpatterns = [
    path('<slug:collection_id>/', views.Recommend.as_view(), name='recommend'),
    path('test/<slug:collection_id>/', views.RecommendTest.as_view(), name='recommend_test'),
]

