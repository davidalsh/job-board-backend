from rest_framework import serializers
from jobs.models import Job


class NewestJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'id',
            'title',
            'position_salary',
            'position_location',
            'company_name',
            'created_at_formatted',
        )


class JobSerializer(serializers.ModelSerializer):
    created_at_formatted = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = '__all__'

    def get_created_at_formatted(self, obj):
        return obj.created_at_formatted()
