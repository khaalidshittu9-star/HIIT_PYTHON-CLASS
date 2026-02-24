from django.urls import path
from .views import note_list, note_detail, create_note, edit_note, delete_note
urlpatterns = [
    path('', note_list, name='note_list'), 
    path('<int:pk>/', note_detail, name='note_detail'),
    path('create/', create_note, name='create_note'),
    path('<int:pk>/edit/' , edit_note, name= 'edit_note') ,
    path('<int:pk>/delete/' , delete_note, name= 'delete_note'),
 ]   


