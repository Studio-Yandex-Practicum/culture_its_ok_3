from rest_framework import serializers
from google_api.models import UserFeedback, ExhibitComment, RouteReview
from excursion.models import Route, Exhibit


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'


class ExhibitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibit
        fields = '__all__'


class UserFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFeedback
        fields = '__all__'


class ExhibitCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExhibitComment
        fields = '__all__'


class RouteReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteReview
        fields = '__all__'
