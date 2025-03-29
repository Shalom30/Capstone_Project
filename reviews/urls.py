from django.urls import path
from .views import (
    ReviewListCreateView, ReviewDetailView, UserListCreateView, UserDetailView,
    review_list, review_create, review_update, review_delete
)

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-api'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail-api'),
    path('', review_list, name='review-list'),
    path('reviews/create/', review_create, name='review-create'),
    path('reviews/<int:pk>/update/', review_update, name='review-update'),
    path('reviews/<int:pk>/delete/', review_delete, name='review-delete'),
]