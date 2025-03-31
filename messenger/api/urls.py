from django.urls import path
from .views import PostList, PostDetail, CommentCreate, UserCreate
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', CommentCreate.as_view(), name='comment-create'),
    path('register/', UserCreate.as_view(), name='user-register'),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
]