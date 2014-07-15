from django.db import models
from content.models import Category
# Create your models here.

class Position(models.Model):
  label = models.CharField(max_length=1,unique=True)
  category = models.ForeignKey(Category, null=True, blank=True)
