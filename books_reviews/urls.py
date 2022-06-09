from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewListView.as_view(), name='home'),  # home page
    path('review/<int:pk>', views.ReviewDetailView.as_view(), name='review-detail'),  # review details
    path('addReview/', views.AddReviewView.as_view(), name='add-review'),  # add review
    path('updateReview/<int:pk>', views.UpdateReviewView.as_view(), name='update-review'),  # update review
    path('deleteReview/<int:pk>', views.DeleteReviewView.as_view(), name='delete-review'),  # delete review
    path('myReviews/', views.UserReviewListView.as_view(), name='user-reviews'),  # user's reviews
    path('searchReview/', views.SearchReviewView.as_view(), name='search-review'),  # search review by book's title
    path('userReviews/<int:pk>', views.UserIdReviewsView.as_view(), name='user-id-reviews'),     # reviews by user id
    # path('bookTitle/<str:book_title>', views.BookTitleView.as_view(), name='book-title')  # reviews by book title

]
