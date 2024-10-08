from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password=None, **extra_fields):
        if password is None:
            raise TypeError('Superusers must have a password.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        if password is None:
            raise TypeError('Users must have a password.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractUser):

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='animania_users',  # Change this to avoid conflict
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='animania_users_permissions',  # Change this to avoid conflict
        blank=True,
        help_text='Specific permissions for this user.'
    )

    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(unique=True, null=True)
    avatar = models.ImageField(null=True, default="pfp.jpg")
    
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    objects = CustomUserManager()
    
class Topic(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Room(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)

    name=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)

    participants=models.ManyToManyField(User,related_name='participants',blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-updated','-created']
        
    def __str__(self):
        return self.name
# Create your models here.
class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)

    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-updated','-created']

    def __str__(self):
        return self.body[0:50]
    
# class Category(models.Model):
#     name = models.CharField(max_length=200)
#     image1 = models.ImageField(null=True)
#     name1 = models.CharField(null=True,max_length=200)
#     image2 = models.ImageField(null=True)
#     name2 = models.CharField(null=True,max_length=200)
#     image3 = models.ImageField(null=True)
#     name3 = models.CharField(null=True,max_length=200)

#     def __str__(self):
#         return self.name

class Enquiry(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, null=True)
    body = models.TextField()

    def __str__(self):
        return self.name