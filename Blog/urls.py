
from django.urls import path, include
from froala_editor import views
from . import views 

urlpatterns = [
    path("", views.BlogPostView.as_view(), name="blog_post"),
    path('froala_editor/', include('froala_editor.urls')),
]
