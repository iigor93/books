from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("start_page.urls")),
    path('books/', include("book.urls")),
    path('user_profile/', include("user_profile.urls")),
]
