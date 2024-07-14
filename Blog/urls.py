
from django.urls import path, include
# from django.conf.urls import url
from froala_editor import views
from . import views 

urlpatterns = [
    path('froala_editor/', include('froala_editor.urls')),
    path("", views.BlogHomeView.as_view(), name="blog_home"),
    path("post/", views.BlogPostView.as_view(), name="blog_post"),
    path('list/', views.BlogListView.as_view(), name="blog_list"),
    path('details/<slug:slug>/', views.BlogDetailView.as_view(), name="blog_detail"),
    path('update/<slug:slug>/', views.BlogUpdateView.as_view(), name="blog_update"),
    path('delete/<slug:slug>/', views.BlogDeleteView.as_view(), name="blog_delete"),
    path('register/', views.RegistrationView.as_view(), name="register"),
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('logout/', views.UserLogoutView.as_view(), name="logout"),
    path('pass_update/<slug:slug>', views.PasswordUpdateView.as_view(), name="pass_update"),
    
]
