from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('user/register/', views.UserCreateView.as_view(), name='user-register'),
    path('token/', TokenObtainPairView.as_view(), name='get_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('thoughts/', views.ThoughtsListCreateView.as_view(), name='thought-list-create'),
    path('thoughts/<int:pk>/delete/', views.NoteDelete.as_view(), name='thought-delete'),
    path('messages/', views.MessageListCreate.as_view(), name='message-list-create'),
]