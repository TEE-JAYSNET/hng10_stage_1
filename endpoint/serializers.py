from rest_framework import serializers
from .models import Stageone


class StageoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stageone
        fields = ('slack_name', 'current_day', 'utc_time', 'track',
                  'github_file_url', 'github_repo_url', 'status_code')
