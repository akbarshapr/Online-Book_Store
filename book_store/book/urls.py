from django.urls import path
from .views import HomePageView, BookList, BookDetail, MyProfileView, MyProfileCreate, MyProfileUpdate, \
    toggle_favorite, cart, add_to_cart, remove_from_cart

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('booklist/', BookList.as_view(), name='books'),
    path('bookdetail/<int:pk>/', BookDetail.as_view(), name='bookdetail'),
    path('add_favorite/<int:book_id>/', toggle_favorite, name='toggle_favorite'),

    path('myprofile/', MyProfileView.as_view(), name='myprofile'),
    path('createprofile/', MyProfileCreate.as_view(), name='createprofile'),
    path('editprofile/', MyProfileUpdate.as_view(), name='editprofile'),

    path('cart/', cart, name='mycart'),
    path('cart/add/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:book_id>/', remove_from_cart, name='remove_from_cart'),

]
