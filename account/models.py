from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Kullanıcılar'

    def __str__(self):
        return self.username

# bunu migrate etmiyoruz, settings'te AUTH_USER_MODEL adında değişken tanımlıyoruz. Daha sonra migrate !
