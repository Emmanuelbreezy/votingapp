import secrets
import os
import random
import datetime
from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator

from users.models import User

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def user_dir_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_path = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "elections/{final_path}".format(final_path=final_path)
  
def user_cand_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_path = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "candidates/{final_path}".format(final_path=final_path)
  
# Create your models here.
class Election(models.Model):
    election_name = models.CharField(max_length=50, blank=False)
    cover_img   =  models.ImageField(upload_to = user_dir_path,blank=True)
    url_extid         = models.SlugField(blank=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return self.election_name


class Candidate(models.Model):
    election = models.ForeignKey(Election,null=True,on_delete=models.CASCADE)
    candidate_name  = models.CharField(max_length=50, blank=False)
    candidate_img   =  models.ImageField(upload_to = user_cand_path,blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    posted_by      = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return self.candidate_name
    

class Vote(models.Model):
    user   = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.email


def election_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.url_extid:
        instance.url_extid = secrets.token_urlsafe(5)


pre_save.connect(election_pre_save_receiver, sender=Election)

    




