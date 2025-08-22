from django.urls import path
from .views import (
    UrlCreate,
    UrlRetrieve,
    UrlDelete,
    UrlUpdate,
    UrlStats
)

urlpatterns = [
    path('shorten/', UrlCreate.as_view(), name='create' ),
    path('shorten/<str:short_code>/', UrlRetrieve.as_view(), name='retrieve' ),
    path('shorten/<str:short_code>/update/', UrlUpdate.as_view(), name='update' ),
    path('shorten/<str:short_code>/delete/', UrlDelete.as_view(), name='delete' ),
    path('shorten/<str:short_code>/stats/', UrlStats.as_view(), name='stats' ),
]
