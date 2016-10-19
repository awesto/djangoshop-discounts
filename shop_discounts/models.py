# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth.models import Group
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class CustomerRebateBase(models.Model):
    percentage = models.DecimalField(_("Rebate in %"), max_digits=4, decimal_places=2)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_("Customers"), blank=True)
    groups = models.ManyToManyField(Group, verbose_name=_("Groups"), blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.identifier


_identifier_help_text = _("Rebate identifier will be shown on invoice")

if settings.USE_I18N:

    if 'parler' not in settings.INSTALLED_APPS:
        raise ImproperlyConfigured("Requires `django-parler`, if configured as multilingual project")

    from parler.models import TranslatableModelMixin, TranslatedFieldsModel, TranslatableManager
    from parler.fields import TranslatedField

    class CustomerRebate(TranslatableModelMixin, CustomerRebateBase):
        identifier = TranslatedField()

        objects = TranslatableManager()

        class Meta:
            app_label = 'shop'
            db_table = 'shop_i18n_customerrebate'
            verbose_name = _("Customer Rebate")
            verbose_name_plural = _("Customer Rebates")

    class CustomerRebateTranslation(TranslatedFieldsModel):
        master = models.ForeignKey(CustomerRebate, related_name='translations', null=True)
        identifier = models.CharField(_("Identifier"), max_length=50, help_text=_identifier_help_text)

        class Meta:
            app_label = 'shop'
            db_table = 'shop_i18n_customerrebate_translation'
            unique_together = [('language_code', 'master')]

else:

    class CustomerRebate(CustomerRebateBase):
        identifier = models.CharField(_("Identifier"), max_length=50, help_text=_identifier_help_text)

        class Meta:
            app_label = 'shop'
            db_table = 'shop_customerrebate'
            verbose_name = _("Customer Rebate")
            verbose_name_plural = _("Customer Rebates")
