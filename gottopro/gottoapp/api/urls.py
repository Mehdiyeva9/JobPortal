from django.conf import urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from gottoapp.api import views

urlpatterns = [
    path('user-create/', views.UserCreateAPIView.as_view()),
    path('category-job-list/<id>/', views.CategoryJobListAPIView.as_view()),
    path('company-job-list/<id>/', views.CompanyJobListAPIView.as_view()),
    path('best-service-list/', views.BestServiceListAPIView.as_view()),
    path('settings-list/', views.SiteSettingsListAPIView.as_view()),
    path('featured-job-list/', views.FeaturedJobsListAPIView.as_view()),
    path('recent-job-list/', views.RecentJobsListAPIView.as_view()),
    path('testimonial-list/', views.TestimonialListAPIView.as_view()),
    path('social-media-list/', views.SocialMediaListAPIView.as_view()),
    path('job-retrieve/<id>/', views.JobRetrieveAPIView.as_view()),
    path('message-create/', views.MessageCreateAPIView.as_view()),
    path('user-favoritelist/', views.UserFavoriteListListAPİView.as_view()),
    path('favoritelist-list/', views.FavoriteListListAPIView.as_view()),
    path('favoritelist-create/', views.FavoriteListCreateAPIView.as_view()),
    path('user-savelist/', views.UserSaveListListAPİView.as_view()),
    path('savelist-list/', views.SaveListListAPIView.as_view()),
    path('savelist-create/', views.SaveListCreateAPIView.as_view()),
 ]