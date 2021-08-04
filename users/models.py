import secrets
import os
import random
import datetime
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db.models.signals import pre_save

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def user_directory_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_path = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "user/{final_path}".format(final_path=final_path)
  
class UserManager(BaseUserManager):
    def create_user(self, email, is_active=True, password=None, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have email address")
        if not password:
            raise ValueError("Users must have Password")

        user_obj = self.model(
            email = self.normalize_email(email),
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj
    
    def create_staffuser(self,email, password=None):
        user = self.create_user(
           email=email,
           password=password,
           is_staff=True
           )
        return user

    def create_superuser(self,email, password=None):
        user = self.create_user(
            email=email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user

# Create your models here.
class User(AbstractBaseUser):
    email = models.CharField(unique=True, max_length=50,blank=False)
    password = models.CharField(max_length=50,blank=False)
    staff      = models.BooleanField(default=False)
    admin      = models.BooleanField(default=False)
    active     = models.BooleanField(default=True)
    timestamp  = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = [] #

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
    

class Profile(models.Model):
    user = models.OneToOneField(User,null=True, related_name="profile_user", on_delete=models.SET_NULL)
    token = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=50,blank=True,)
    firstname = models.CharField(max_length=50,blank=True,)
    lastname = models.CharField(max_length=50,blank=True,)
    dob = models.DateField(blank=True)
    localgovernment = models.CharField(max_length=100,blank=False,)
    fingerprintID = models.CharField(max_length=100, blank=True,)
    photo = models.ImageField(upload_to=user_directory_path,blank=True)
    timestamp  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname

def profile_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.token:
        instance.token = secrets.token_hex(8)

 
pre_save.connect(profile_pre_save_receiver, sender=Profile) 