from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)

    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=4, blank=True)
    tagline = models.CharField(max_length=40, blank=True)

    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    #auto_now_add mowi Django aby ustawil automatycznie date podczas utworzenia obiektu i nie edytowal jej pozniej
    updated_at = models.DateTimeField(auto_now=True) #Django zmienia date za kazdym razem gdy obiekt jest zapisywany

    objects = AccountManager()

    USERNAME_FIELD = 'email' #mowimy django, ze chcemy aby traktowal adres email jako nazwe uzytkownika
    REQUIRED_FIELDS = ['username'] #konieczne podczas zastepowania modelu USER

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name
