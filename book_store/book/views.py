from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect

from .models import Book, MyProfile, Review

from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'main/home.html'


class BookList(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book/booklist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['books'] = context['books'].filter(
                Q(title__icontains=search_input) | Q(author__icontains=search_input))
        context['search_input'] = search_input
        return context


class BookDetail(LoginRequiredMixin, DetailView):
    model = Book
    context_object_name = 'books'
    template_name = 'book/bookdetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all()
        return context


def like_review(request):
    if request.method == 'POST':
        review_id = request.POST.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        review.like()
        return redirect('bookdetail', pk=review.book.pk)


class MyProfileView(LoginRequiredMixin, ListView):
    model = MyProfile
    context_object_name = 'myprofile'
    template_name = 'book/my_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myprofile'] = context['myprofile'].filter(user=self.request.user)
        return context


class MyProfileCreate(LoginRequiredMixin, CreateView):
    model = MyProfile
    fields = ['name', 'email', 'pfp', 'bio', 'favorites', 'delivery_address']
    success_url = reverse_lazy('myprofile')
    template_name = 'book/create_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MyProfileCreate, self).form_valid(form)
