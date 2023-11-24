from django.urls import path, include
# app_name = "api"
urlpatterns = [
    path('event/', include('events.urls')),
    path('blog/', include('blogs.urls')),
    
           
]



    