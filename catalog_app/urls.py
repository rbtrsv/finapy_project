from django.urls import path
from . import views

app_name = "catalog_app"

urlpatterns = [
    # Create a placeholder file for the URLConf module
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    # re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    # path('url/', views.my_reused_view, {'my_template_name': 'some_path'}, name='aurl'),
    # path('anotherurl/', views.my_reused_view, {'my_template_name': 'another_path'}, name='anotherurl'),
]

urlpatterns += [   
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    # path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),  # Added for challenge
]

urlpatterns += [   
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]

urlpatterns += [  
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]

# Add URLConf to create, update, and delete books
# urlpatterns += [
#     path('book/create/', views.BookCreate.as_view(), name='book_create'),
#     path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
#     path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
# ]