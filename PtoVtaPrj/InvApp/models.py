from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.company.name}"

class Inventory(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.item_name} - {self.company.name}"
