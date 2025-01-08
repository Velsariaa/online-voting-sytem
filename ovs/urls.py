from django.urls import path
from . import views

urlpatterns = [
    path('adminnform', views.admin_form_view, name='adminnform'),
    path('registrationform', views.registration_form_view, name='registrationform'),
    path('loginform', views.login_form_view, name='loginform'),
    path('contactform', views.contact_form_view, name='contactform'),
    path('candidacyform', views.candidacy_form_view, name='candidacyform'),
    path('credentialsform', views.credentials_form_view, name='credentialsform'),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('comelec', views.user_management_view, name='comelec'),
    path('resetpass', views.reset_form_view, name='resetpass'), 
    path('user', views.user, name='user'), 
    path('vote', views.vote, name='vote'), 
    path('submitted', views.submitted, name='submitted'), 
    path('inheritance', views.inheritance, name='inheritance'),
    path('update/<int:pk>', views.user_management_update, name='update'),
    path('delete/<int:pk>', views.user_management_delete, name='delete'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Admin dashboard
    path('manage-movies/', views.dashboard, name='manage_movies'),  # Placeholder for Manage Movies view
    path('user-table/', views.dashboard, name='user_table'),  # Placeholder for User Table view
    path('logout/', views.logoutUser, name='logout'),
    path('candidacy-form/', views.candidacy_form_view, name='candidacy_form'),
    
]
