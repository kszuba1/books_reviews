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
    success_url = reverse_lazy('home')






