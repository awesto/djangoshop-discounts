# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from shop.modifiers.base import BaseCartModifier
from shop.rest.serializers import ExtraCartRow
from shop_discounts.models import CustomerRebate


class CustomerRebateModifier(BaseCartModifier):
    """
    Cart modifier which handles rebates based on the current customer.
    """
    identifier = 'customer-rebate'
    commision_percentage = None

    def add_extra_cart_row(self, cart, request):
        if request.customer.is_authenticated():
            filter = Q(groups__in=request.customer.groups.all()) | Q(users=request.user)
            queryset = CustomerRebate.objects.filter(filter)
            if queryset:
                rebate = queryset.order_by('percentage').last()
                amount = - cart.total * rebate.percentage / 100
                label = _("{percentage:.0f}%% rebate for {rebate}").format(percentage=rebate.percentage,
                                                                      rebate=str(rebate))
                cart.extra_rows[self.identifier] = ExtraCartRow({'label': label, 'amount': amount})
                cart.total += amount
