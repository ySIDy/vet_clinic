from django.db import models

# Create your models here.
class CustomerContact(models.Model):
    user_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.user_name
    
    def save(self, *args, **kwargs):
        super(CustomerContact, self).save(*args, **kwargs)


class User(models.Model):
    user_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.user_name
    
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)