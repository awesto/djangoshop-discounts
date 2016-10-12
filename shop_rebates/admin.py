# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from shop_rebates.models import CustomerRebate


@admin.register(CustomerRebate)
class CustomerRebateAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'get_rebate')
    filter_horizontal = ('users', 'groups')

    def get_rebate(self, obj):
        return '{} %'.format(obj.percentage)
    get_rebate.short_description = _("Rebate")
