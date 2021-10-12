from authApp.models.profile import Profile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['birth_date', 'gender', 'country', 'payment_method', 'notification_status', 'plan_type']

