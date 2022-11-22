from django.urls import path
from . import  views

urlpatterns = [
  path("login",views.loginUser,name="login"),
  path("logout",views.logoutUser,name="logout"),
  path("register",views.registerUser,name="register"),
  
  path("",views.profiles,name='profiles'),
  path("user-profile/<str:pk>",views.user_profile,name='user-profile'),
  path("account",views.userAccount,name='account'),
  path("edit-account",views.editAccount,name='edit-account'),

  path('add-skill',views.createSkill,name='add-skill'),
  path('edit-skill/<str:pk>',views.updateSkill,name='edit-skill'),
  path('delete-skill/<str:pk>',views.deleteSkill,name='delete-skill'),

  path('inbox/' ,views.inbox, name='inbox'),
  path('message/<str:pk>' ,views.viewMessage, name='message'),
  path('create-message/<str:pk>' ,views.createMessage, name='create-message'),
  
]

