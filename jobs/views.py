from rest_framework import mixins, viewsets
from rest_framework.viewsets import GenericViewSet

from jobs.models import Job, Category
from jobs.serializers import NewestJobSerializer, JobSerializer


class NewestJobsViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Job.objects.all()[:4]
    serializer_class = NewestJobSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    http_method_names = ['options', 'head', 'get']
