from django.urls import include, path
from apps.recommend import views

app_name = 'recommend'

urlpatterns = [
    path('<int:pk>/', views.Recommend.as_view(), name='recommend'),
    path('test/<int:pk>/', views.RecommendTest.as_view(), name='recommend_test'),
]

