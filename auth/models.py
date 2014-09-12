from django.contrib.auth.models import User
from django.db import models

#Modelo para los usuarios del sitio, este modelo extiende el modelo de usuarios de Django
class SiteUser(User):
    models.ImageField(upload_to='uploads/avatars', null=True, blank=True).contribute_to_class(User,'avatar')
