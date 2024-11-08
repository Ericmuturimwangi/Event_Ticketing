from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from events.views import EventViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls, name='admin'),
    path('api/', include (router.urls)),
    path('api/users/', include('users.urls')),

]
