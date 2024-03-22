from django.urls import path
from .views import index, create, edit

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('edit/<int:user_id>', edit, name='edit')

]