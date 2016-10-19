# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from shop_discounts.models import CustomerRebate


class CustomerRebateAdminBase(admin.ModelAdmin):
    list_display = ('identifier', 'get_rebate',)
    filter_horizontal = ('users', 'groups',)

    def get_rebate(self, obj):
        return '{} %'.format(obj.percentage)
    get_rebate.short_description = _("Rebate")


if settings.USE_I18N:
    from parler.admin import TranslatableAdmin

    class CustomerRebateAdmin(TranslatableAdmin, CustomerRebateAdminBase):
        fieldsets = (
            (_("Translatable Fields"), {
                'fields': ('identifier',)
            }),
            (_("Rebates for"), {
                'fields': ('percentage', 'users', 'groups',),
            }),
        )

else:

    class CustomerRebateAdmin(CustomerRebateAdminBase):
        fields = ('identifier', 'percentage', 'users', 'groups',)

admin.site.register(CustomerRebate, CustomerRebateAdmin)
