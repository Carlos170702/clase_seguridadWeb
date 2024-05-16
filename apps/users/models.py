from django.db import models

# Create your models here.


class UserModel(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    username = models.CharField(null=False, blank=False, max_length=100)
    password = models.CharField(null=False, blank=False, max_length=20)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(null=False, blank=False, max_length=50)

    required_fields = ['name', 'username', 'password', 'email']

    def __str__(self):
        return self.username
