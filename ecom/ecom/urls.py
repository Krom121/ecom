from django.contrib import admin
from django.urls import path, include

app_name = 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('blog/', include('blog.urls', namespace='blog')),
]
