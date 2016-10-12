# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import Group
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class CustomerRebate(models.Model):
    identifier = models.CharField(_("Identifier"), max_length=50)
    percentage = models.DecimalField(_("Rebate in %"), max_digits=4, decimal_places=2)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_("Customers"), blank=True)
    groups = models.ManyToManyField(Group, verbose_name=_("Groups"), blank=True)

    class Meta:
        app_label = 'shop'
        db_table = 'shop_customerrebate'
        verbose_name = _("Customer Rebate")
        verbose_name_plural = _("Customer Rebates")

    def __str__(self):
        return self.identifier
