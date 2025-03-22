# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Category(models.Model):

    #__Category_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Category_FIELDS__END

    class Meta:
        verbose_name        = _("Category")
        verbose_name_plural = _("Category")


class Attribut(models.Model):

    #__Attribut_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Attribut_FIELDS__END

    class Meta:
        verbose_name        = _("Attribut")
        verbose_name_plural = _("Attribut")


class Modele(models.Model):

    #__Modele_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    #__Modele_FIELDS__END

    class Meta:
        verbose_name        = _("Modele")
        verbose_name_plural = _("Modele")



#__MODELS__END
