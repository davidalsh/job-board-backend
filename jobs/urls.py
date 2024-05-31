from rest_framework.routers import DefaultRouter

from jobs.views import NewestJobsViewSet, JobViewSet

router = DefaultRouter()
router.register('newest', NewestJobsViewSet, basename='newest_jobs')
router.register('', JobViewSet, basename='jobs')
