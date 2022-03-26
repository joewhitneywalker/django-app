from django.urls import path
from . import views

#SIMILAR TO APP.USE() IN EXPRESS


urlpatterns = [#characters  urls
    path('', views.Home.as_view(), name="home"), #home 
    path('characters/', views.Character_List.as_view(), name="character_list"), #path to render all character
    path('about/', views.About.as_view(), name="about"), # <- new route,
    path('characters/new/', views.Character_Create.as_view(), name="character_create"), #path to create new character
    path('characters/<int:pk>/', views.Character_Detail.as_view(), name="character_detail"),
    path('characters/<int:pk>/update', views.Character_Update.as_view(), name = "character_update"),
    path('characters/<int:pk>delete', views.Character_Delete.as_view(), name="character_delete"),
    path('user/<username>/', views.profile, name='profile'),
    path('characterpowers/', views.characterpowers_index, name='characterpowers_index'),
    path('characterpowers/<int:characterpowers_id>', views.characterpowers_show, name='characterpowers_show'),
    path('characterpowers/create/', views.CharacterPowersCreate.as_view(), name='characterpowers_create'),
    path('characterpowers/<int:pk>/update/', views.CharacterPowersUpdate.as_view(), name='characterpowers_update'),
    path('characterpowers/<int:pk>/delete/', views.CharacterPowersDelete.as_view(), name='characterpowers_delete'),
    #login authorization
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]



 #commenting out the below which was in notion but throwing errors. in the practice, Rome did not use these
    #path('', views.index, name='index'),
    #path('<int:character_id>/', views.show, name='show'),
    #path('post_url/', views.post_character, name='post_character'),