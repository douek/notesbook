from django.urls import path
from app import views

urlpatterns = [
    path('notes/', views.notes_list),
    path('notes/<int:note_id>/', views.note_detail),
    path('notes/user/<int:user_id>/', views.user_notes),
    path('users/<int:profile_id>/', views.user_profile),
]