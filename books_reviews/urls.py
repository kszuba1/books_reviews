from django.urls import path
# from . import views
from .views import Home, ReviewDetail, AddReview, UpdateReview, DeleteReview

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    path('addReview/', AddReview.as_view(), name='add-review'),
    path('updateReview/<int:pk>', UpdateReview.as_view(), name='update-review'),
    path('deleteReview/<int:pk>', DeleteReview.as_view(), name='delete-review'),
]
