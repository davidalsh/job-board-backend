from django.contrib import admin
from django.urls import path, include
from jobs.urls import router as jobs_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/jobs/', include(jobs_router.urls)),
]
