from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Review
from .serializers import ReviewSerializer, UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm  # Assuming this exists

# Custom permission for review ownership
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # GET allowed for all
            return True
        return obj.user == request.user  # Only owner can modify/delete

# User CRUD
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated users can list/create

    def perform_create(self, serializer):
        serializer.save()  # Password hashing handled in serializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated users can access

    def perform_update(self, serializer):
        if self.request.user != serializer.instance and not self.request.user.is_staff:
            raise permissions.PermissionDenied("You can only update your own profile.")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user != instance and not self.request.user.is_staff:
            raise permissions.PermissionDenied("You can only delete your own profile.")
        instance.delete()

# Review CRUD
class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['movie_title', 'rating']
    search_fields = ['movie_title', 'review_content']
    ordering_fields = ['rating', 'created_date']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Set user to current authenticated user

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]  # Add ownership check

# Template Views (unchanged)
def review_list(request):
    reviews = Review.objects.all()
    if request.GET.get('search'):
        reviews = reviews.filter(movie_title__icontains=request.GET['search'])
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

@login_required
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review-list')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form})

@login_required
def review_update(request, pk):
    review = Review.objects.get(pk=pk)
    if review.user != request.user:
        return redirect('review-list')
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review-list')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/review_form.html', {'form': form})

@login_required
def review_delete(request, pk):
    review = Review.objects.get(pk=pk)
    if review.user != request.user:
        return redirect('review-list')
    if request.method == 'POST':
        review.delete()
        return redirect('review-list')
    return render(request, 'reviews/review_confirm_delete.html', {'review': review})