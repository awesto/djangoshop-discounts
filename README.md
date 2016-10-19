# Customer Rebates for django-SHOP

This integration only works for django-SHOP version 0.9 and above.


## Installation

In ``settings.py`` add ``'shop_discounts'`` to ``INSTALLED_APPS``.

Additionally add to

```
SHOP_CART_MODIFIERS = (
    ...
    'shop_discounts.modifiers.CustomerRebateModifier',
    ...
)
```

The position of this rebate modifier is important. Add it after the ``DefaultCartModifier``, but
before the taxes and shipping modifiers. 


## Usage

In Django's admin backend, below section **Shop**, add a Customer Rebate object. The identifier of
this rebate will be printed on the invoice in section extra cart rows.

Then choose the rebate percentage and the customers or group of customers to whom this rebate shall
apply.

Note: If more than one rebate applies for the purchasing customer, then that one with the highest
percentage is selected. Rebates are not stacked!
