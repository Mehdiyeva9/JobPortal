from django.contrib import admin
from gottoapp.models import (
    Category, BestService, Profession, Type, Company, Job, Favoritelist, 
    Savelist, Testimonial, Message, SiteSettings, SocialMedia
    )

admin.site.register(Category)
admin.site.register(BestService)
admin.site.register(Profession)
admin.site.register(Type)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "mail", "address" )
    list_display_links = ("address", )
    list_editable = ("mail", )
    search_fields = ("name", )
    #fields = ("name", )
    fieldsets = (
        ("Əsas parametrlər", {"fields": ("name", "logo")}),
        ("Digər parametrlər", {"fields": ("about", "address","phone", "mail" )}),
    )
# admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Favoritelist)
admin.site.register(Savelist)
admin.site.register(Testimonial)
admin.site.register(Message)
#admin.site.register(SiteSettings)

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self,request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
    
    def has_delete_permission(self, request, obj = ...):
        return False

admin.site.register(SocialMedia)