from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import ReviewForm
from .models import Review
from django.http import HttpResponse, request
from django.views import generic


# all reviews


class Home(generic.ListView):
    model = Review
    template_name = 'home.html'
    ordering = ['-id']


class AddReview(generic.CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review-form.html'

    # fields = '__all__'

    def form_valid(self, form):  # set reviews.user as current user
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReviewDetail(generic.DetailView):
    model = Review
    template_name = 'review-details.html'


class UpdateReview(generic.UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review-form.html'
    # template_name = 'update-form.html'
    # fields = ['title', 'book_title', 'book_author', 'description', 'rate']


class DeleteReview(generic.DeleteView):
    model = Review
    template_name = 'delete-review.html'
    success_url = reverse_lazy('home')


class UserReviews(generic.ListView):
    model = Review
    template_name = 'user-reviews.html'

    def get_queryset(self):
        return Review.objects.filter(  # all user reviews, sorted by the latest
            user=self.request.user).order_by('-id')


class SearchReview(generic.ListView):
    model = Review
    template_name = 'search-review.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):

        query = self.request.GET.get('search')

        if query:
            result = Review.objects.filter(book_title__contains=query)

        else:
            result = None

        return result
