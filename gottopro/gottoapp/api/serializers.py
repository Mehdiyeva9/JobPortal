from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from gottoapp.models import (
    Category, BestService, Profession, Type, Company, Job, Favoritelist, 
    Savelist, Testimonial, Message, SiteSettings, SocialMedia
    )

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ("username", "password")

    def validate(self, data):
        validate_password(data['password'])
        return data
    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]

        user = User.objects.create_user(
            username = username,
            password = password
        )
        return user
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class BestServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestService
        fields = "__all__"

class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = "__all__"

class CompanyLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("logo", )

class FeaturedJobsSerializer(serializers.ModelSerializer):
    company = CompanyLogoSerializer()
    class Meta:
        model = Job
        fields = ("name", "location", "created_at", "salary", "profession", "type" )

class RecentJobsSerializer(serializers.ModelSerializer):
    company = CompanyLogoSerializer()
    class Meta:
        model = Job
        fields = ("image", "name", "location", "created_at", "salary", "profession", "type" )

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = "__all__"

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

class FavoriteListSerializer(serializers.ModelSerializer):
    job = JobSerializer()
    user = UserCreateSerializer()
    class Meta:
        model = Favoritelist
        fields = "__all__"

class FavoriteListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoritelist
        fields = ("job", )

class SaveListSerializer(serializers.ModelSerializer):
    job = JobSerializer()
    user = UserCreateSerializer()
    class Meta:
        model = Savelist
        fields = "__all__"

class SaveListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savelist
        fields = ("job", )

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
