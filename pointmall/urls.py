
from django.contrib import admin
from django.urls import path, include

from pointmall import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls.user_urls')),
    path('items/', include('item.urls.item_urls')),
    path('categorys/', include('item.urls.category_urls')),
    path('media/uploads/item_images/<str:file_name>', views.image_view),
    path('me/', include('user.urls.me_urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
