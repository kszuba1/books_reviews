from django.urls import path
# from . import views
from .views import Home, ReviewDetail, AddReview, UpdateReview, DeleteReview, UserReviews, SearchReview

urlpatterns = [
    path('', Home.as_view(), name='home'),  # home page
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),   # review details
    path('addReview/', AddReview.as_view(), name='add-review'),   # add review
    path('updateReview/<int:pk>', UpdateReview.as_view(), name='update-review'),   # update review
    path('deleteReview/<int:pk>', DeleteReview.as_view(), name='delete-review'),   # delete review
    path('myReviews/', UserReviews.as_view(), name='user-reviews')  ,  # user's reviews
    path('searchReview/', SearchReview.as_view(), name='search-review'),
]
