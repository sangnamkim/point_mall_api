from django.urls import path

from user import views


urlpatterns = [
    path('items/', views.MyItemView.as_view()),
    path('', views.MeView.as_view())
]