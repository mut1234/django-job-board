from django.db import models

'''
django model filed:
-html widget
-validation
-db size
'''

# Create your models here.

JOB_TYPE=(
    ('Full Iime','Full Iime'),
    ('Part Iime','Part Iime'),

)
class Job(models.Model): #table
    title = models.CharField(max_length=100) #column
    job_type = models.CharField(max_length=15 ,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True) #auto_now time of add \ auto_now_add time of last edit
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE) # 1 to many
    def __str__(self): 
        return self.title # to return title instead than object

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name