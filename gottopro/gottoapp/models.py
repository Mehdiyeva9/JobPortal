from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=15)
    icon = models.TextField(blank=True, null=True)
    number_of_ad = models.IntegerField(default=0)

    class Meta:
        ordering = ('-id', )
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class BestService(models.Model):
    icon = models.ImageField(upload_to='gotto_imgs/')
    title = models.CharField(max_length=15)
    content = models.TextField()

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return self.title

class Profession(models.Model):
    name = models.TextField()

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return self.name
    
class Type(models.Model):
    name = models.TextField()

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return self.name

class Company(models.Model):
    logo = models.ImageField(upload_to='gotto_imgs/')
    name = models.CharField(max_length=20)
    about = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=14)
    mail = models.EmailField(max_length=256)

    class Meta:
        ordering = ('-id', )
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

class Job(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jobs')
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='gotto_imgs/')
    content = models.TextField()
    location = models.TextField()
    salary = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, related_name='jobs')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='jobs')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return self.name
    
class Favoritelist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_favori_job')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_favori_items')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return self.job
    
class Savelist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_save_job')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_save_items')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return self.job

class Testimonial(models.Model):
    name = models.CharField(max_length=20)
    profession = models.TextField()
    raiting = models.IntegerField(default=0)
    content = models.TextField()

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.CharField(max_length=15)
    mail = models.EmailField(max_length=256)
    content = models.TextField()

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return self.name

class SiteSettings(models.Model):
    logo = models.ImageField(upload_to='gotto_imgs/', blank=True, null=True)
    headtitle = models.TextField(blank=True, null=True)
    headcontent = models.TextField(blank=True, null=True)
    about_title = models.CharField(max_length=20, blank=True, null=True)
    about_subtitle = models.TextField(blank=True, null=True)
    about_content = models.TextField(blank=True, null=True)
    about_image = models.ImageField(upload_to='gotto_imgs/', blank=True, null=True)
    about_image_title = models.TextField(blank=True, null=True)
    personal_name = models.CharField(max_length=20,blank=True, null=True)
    personal_profession = models.CharField(max_length=15, blank=True, null=True)
    personal_image = models.ImageField(upload_to='gotto_imgs/', blank=True, null=True)
    middle_title = models.TextField(blank=True, null=True)
    middle_content = models.TextField(blank=True, null=True)
    daily_users = models.IntegerField(default=0, blank=True, null=True)
    opening_jobs = models.IntegerField(default=0, blank=True, null=True)
    video = models.FileField(upload_to='gotto_imgs/', blank=True, null=True)
    foot_title = models.TextField(blank=True, null=True)
    foot_content = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mail = models.EmailField(max_length=256, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Settings"

    def __str__(self):
        return "Settings"

    def save(self, *args, **kwargs):
        if not self.id and SiteSettings.objects.exists():
            pass
        return super(SiteSettings, self).save(*args, **kwargs)
    
class SocialMedia(models.Model):
    link = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return self.link