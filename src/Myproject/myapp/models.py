from django.db import models
from django.contrib.auth.models import BaseUserManager #is used to create a Manager for the model
from django.contrib.auth.models import PermissionsMixin #is used to have options to create a user or a superuser
from django.contrib.auth.models import AbstractBaseUser #will be inherited to make the user class



class UserProfileManager(BaseUserManager): # this class manages the UserProfile model

    def create_user(self , email , name , password = None):
        if not email:
            raise ValueError('Email is not enterd')

        email = self.normalize_email(email) # normalizes the email
        user = self.model(email = email , name = name) #creates a model
        user.set_password(password) # sets a crypted password
        user.save(using=self._db) # saves the user in database

        return user

    def create_superuser(self , email , name , password):

        user = self.create_user(email , name , password)
        user.is_superuser = True # the user is a superuser
        user.is_staff=True  # the user is a superuser
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser , PermissionsMixin): # user model class


    email = models.EmailField(max_length=255,unique=True) #each property is set by a field from models class
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False) # is a superuser?
    is_active = models.BooleanField(default=True) #is online?

    objects = UserProfileManager() # tells python how to manage this class

    USERNAME_FIELD='email' # sets the username field
    REQUIRED_FIELDS=['name'] # specifies which fileds are required

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self): # is the ToString method in c#
        return self.email

# Feed model

class Profilefeeditem(models.Model):
        user_profile = models.ForeignKey('UserProfile',on_delete= models.CASCADE)
        status_text = models.CharField(max_length = 255)
        created_on = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.status_text
