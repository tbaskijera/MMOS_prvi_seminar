from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('issued/', views.issued, name='issued'),
    path('persons/', views.persons, name='persons'),
    path('', include('django.contrib.auth.urls')),
    path('books/delete-book/<task_id>', views.delete_book, name='delete_book'),
    path('persons/delete-person/<task_id>', views.delete_person, name='delete_person'),
    path('issued/delete-issued/<task_id>', views.delete_issued, name='delete_issued'),
    path('books/edit-book/<task_id>', views.edit_book, name='edit_book'),
    path('books/edit-person/<task_id>', views.edit_person, name='edit_person'),
    path('books/edit-issued/<task_id>', views.edit_issue, name='edit_issued'),
]