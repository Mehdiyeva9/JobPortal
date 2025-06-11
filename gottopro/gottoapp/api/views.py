from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from gottoapp.models import (
    Category, BestService, Profession, Type, Company, Job, Favoritelist, 
    Savelist, Testimonial, Message, SiteSettings, SocialMedia
    )
from gottoapp.api.serializers import (
    UserCreateSerializer, JobSerializer, BestServiceSerializer, SiteSettingsSerializer, 
    FeaturedJobsSerializer, RecentJobsSerializer, TestimonialSerializer, 
    SocialMediaSerializer, MessageSerializer, FavoriteListSerializer, JobRetrieveSerializer, 
    FavoriteListCreateSerializer, SaveListSerializer, SaveListCreateSerializer)

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class CategoryJobListAPIView(ListAPIView):
    def get_queryset(self):
        category_id = self.kwargs.get("id")
        category = get_object_or_404(Category, id=category_id)
        return Job.objects.filter(
            category = category
        )
    serializer_class = JobSerializer

class CompanyJobListAPIView(ListAPIView):
    def get_queryset(self):
        company_id = self.kwargs.get('id')
        company = get_object_or_404(Company, id=company_id)
        return Job.objects.filter(
            company = company
        )
    serializer_class = JobSerializer

class BestServiceListAPIView(ListAPIView):
    queryset = BestService.objects.all()
    serializer_class = BestServiceSerializer

class SiteSettingsListAPIView(ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer

class FeaturedJobsListAPIView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = FeaturedJobsSerializer

class RecentJobsListAPIView(ListAPIView):
    queryset = Job.objects.all()[:10]
    serializer_class = RecentJobsSerializer

class TestimonialListAPIView(ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class SocialMediaListAPIView(ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

class JobRetrieveAPIView(RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobRetrieveSerializer
    lookup_field = ("id")

class MessageCreateAPIView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class UserFavoriteListListAPİView(ListAPIView):
    def get_queryset(self):
        return Favoritelist.objects.filter(
            user = self.request.user
        )
    serializer_class = FavoriteListSerializer

class FavoriteListListAPIView(ListAPIView):
    queryset = Favoritelist.objects.all()
    serializer_class = FavoriteListSerializer
    permission_classes = (IsAdminUser, )

class FavoriteListCreateAPIView(CreateAPIView):
    queryset = Favoritelist.objects.all()
    serializer_class = FavoriteListCreateSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class UserSaveListListAPİView(ListAPIView):
    def get_queryset(self):
        return Savelist.objects.filter(
            user = self.request.user
        )
    serializer_class = SaveListSerializer

class SaveListListAPIView(ListAPIView):
    queryset = Savelist.objects.all()
    serializer_class = SaveListSerializer
    permission_classes = (IsAdminUser, )

class SaveListCreateAPIView(CreateAPIView):
    queryset = Savelist.objects.all()
    serializer_class = SaveListCreateSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)