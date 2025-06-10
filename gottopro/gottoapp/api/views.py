from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from gottoapp.models import Category, Job, Company

class CategoryJobListAPIView(ListAPIView):
    def get_queryset(self):
        category_id = self.kwargs.get("id")
        category = Category.objects.get(id=category)
        return Job.objects.filter(
            category = category
        )
    serializer_class = JobSerializer

class CompanyJobListAPIView(ListAPIView):
    def get_queryset(self):
        company_id = self.kwargs.get('id')
        company = Company.objects.get(id=company_id)
        return Job.objects.filter(
            company = company
        )
    serializer_class = JobSerializer