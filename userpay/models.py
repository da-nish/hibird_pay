from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
#from django.contrib.auth.models import AbstractUser
# from django.dispatch import receiver
# from django.db.models.signals import post_save

from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True

class Profile(models.Model):
	def file_path(self,filename):
		return "{0}/{1}/{2}".format('users','document',filename)
	packs = (
		('Browse+ | 12MBPS','Browse+ | 12MBPS'),
		('Pace+ | 20MBPS','Pace+ | 20MBPS'),
		('Quick+ | 50MBPS','Quick+ | 50MBPS'),
		)
	def dueDate():
		return timezone.now()+timezone.timedelta(days=30)
	user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='UserID')
	mobile_no = models.CharField(max_length=10)
	gst = models.CharField(max_length=30,verbose_name='GST_No',blank=True,null=True)
	current_plan = models.CharField(max_length=100,choices=packs,default=12)	
	plan_amount = models.PositiveIntegerField()
	address = models.TextField(blank=True,null=True)
	document_no = models.CharField(max_length=20)
	document_front = models.FileField(upload_to = file_path,blank=True)
	document_back = models.FileField(upload_to = file_path,blank=True)
	due_date = models.DateField(default=dueDate)

	def __str__(self):
		return self.user.username

class TransactionDetail(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	order_id = models.CharField(max_length=50)
	payment_id = models.CharField(max_length=50,blank=True,null=True)
	date = models.DateTimeField(null=True,blank=True)
	success = models.BooleanField(default=False)
	amount = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.user.username
# @receiver(post_save,sender=User)
# def username_generation(sender,**kwargs):
# 	if kwargs.get('created'):
# 		instance = kwargs.get('instance')
# 		instance.username = 'Hybrid'+str(instance.id)
# 		instance.save()


class PlanDetail(models.Model):
	title = models.CharField(max_length=20,default='Base')
	month_detail = models.CharField(max_length=20,default='Monthly')
	amount = models.PositiveIntegerField()
	speed_detail = models.PositiveIntegerField(default=0)
	description = models.TextField()
	data_per_month = models.CharField(max_length=10,default='Unlimited')
	offer_detail = models.CharField(max_length=50,default='NA')	

class Slider(models.Model):
	title = models.CharField(max_length=50)
	photo = models.FileField(upload_to='slider/')

	def __str__(self):
		return self.title

class WebSlider(models.Model):
	title = models.CharField(max_length=50,blank=True,null=True)
	photo = models.FileField(upload_to='slider/')


class ContactFormData(models.Model):
	contact_name = models.CharField(max_length=50)
	contact_mobile = models.CharField(max_length=13)
	subject = models.CharField(max_length=50)
	message = models.TextField()

	def __str__(self):
		return self.subject