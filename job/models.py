from django.contrib.auth.models import User
from django.core.files import uploadhandler
from django.db import models
from django.utils.text import slugify
'''
django model filed:
-html widget
-validation
-db size
'''

# Create your models here.

JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),

)
def image_uplaod(instance,filename):
    imagename,extenstion = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extenstion)

class Job(models.Model): #table
    owner = models.ForeignKey(User,related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100) #column
    job_type = models.CharField(max_length=15 ,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True) #auto_now time of add \ auto_now_add time of last edit
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE) # 1 to many
    image = models.ImageField(upload_to=image_uplaod)
    slug =models.SlugField(blank=True,null=True)


    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args, **kwargs)


    def __str__(self): 
        return self.title # to return title instead than object

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Apply(models.Model):
    job=models.fieldName = models.ForeignKey(Job,related_name='apply_job', on_delete=models.CASCADE)
    name =models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    website=models.URLField()
    cv=models.FileField(upload_to='apply/')
    cover_letter=models.TextField(max_length=500) 
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
