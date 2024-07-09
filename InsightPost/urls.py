
from django.contrib import admin
from django.urls import path, include
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Blog.urls")),
    # path('froala_editor/', include('froala_editor.urls')),
    path("admin/", admin.site.urls),
    path('', include('InsightPost.urls')),
]
