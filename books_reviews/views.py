from django.urls import reverse_lazy
from .forms import ReviewForm
from .models import Review
from django.views import generic


# all reviews


class ReviewListView(generic.ListView):
    model = Review
    template_name = 'home.html'
    ordering = ['-id']


class AddReviewView(generic.CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review-form.html'

    # fields = '__all__'

    def form_valid(self, form):  # set reviews.user as current user
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReviewDetailView(generic.DetailView):
    model = Review
    template_name = 'review-details.html'


class UpdateReviewView(generic.UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review-form.html'
    # template_name = 'update-form.html'
    # fields = ['title', 'book_title', 'book_author', 'description', 'rate']


class DeleteReviewView(generic.DeleteView):
    model = Review
    template_name = 'delete-review.html'
    success_url = reverse_lazy('home')


class UserReviewListView(generic.ListView):
    model = Review
    template_name = 'user-reviews.html'
    ordering = ['-id']

    def get_queryset(self):
        return Review.objects.filter(  # all user reviews, sorted by the latest
            user=self.request.user).order_by('-id')


class SearchReviewView(generic.ListView):
    model = Review
    template_name = 'search-review.html'
    context_object_name = 'all_search_results'
    ordering = ['-id']

    def get_queryset(self):

        query = self.request.GET.get('search')

        if query:
            result = Review.objects.filter(book_title__contains=query)  # search reviews by book's title

        else:
            result = None

        return result


class UserIdReviewsView(generic.ListView):
    model = Review
    # template_name = 'user-id-reviews.html'
    context_object_name = 'all_reviews_by_user'
    ordering = ['-id']

    def get_template_names(self):
        if self.request.user.id == self.kwargs['pk']:
            return 'user-reviews.html'
        return 'user-id-reviews.html'

    def get_queryset(self):
        return Review.objects.filter(user=self.kwargs['pk'])


# class BookTitleView(generic.ListView):
#     model = Review
#     template_name = 'home.html'
#     ordering = ['-id']
#
#     def get_queryset(self):
#         return Review.objects.filter(book_title=self.kwargs['pk'])
#
#
#
# class BookAuthorView(generic.ListView):
#     model = Review
#     template_name = 'home.html'
#     ordering = ['-id']
#
#     def get_queryset(self):
#         return Review.objects.filter(user=self.kwargs['pk'])
