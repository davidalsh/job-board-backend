from rest_framework.routers import DefaultRouter

from jobs.views import NewestJobsViewSet, JobViewSet, CategoryViewSet

router = DefaultRouter()
router.register('newest', NewestJobsViewSet, basename='newest_jobs')
router.register('categories', CategoryViewSet, basename='categories')
router.register('', JobViewSet, basename='jobs')
