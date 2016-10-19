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

The discount is computed using the *current* subtotal, then withdrawn from thereof. 
Therefore the position of this rebate modifier is important. Add it after the ``DefaultCartModifier``,
but before your choosen tax modifier. 


## Usage

In Django's admin backend, below section **Home › Shop › Customer Rebates**, add a Customer Rebate
object. The identifier of this rebate will be printed on the invoice in section extra cart rows,
so choose it carefully.

Then choose the rebate percentage and the customers or group of customers to whom this rebate shall
beeing applied.


### Note

> If more than one rebate applies for the purchasing customer, then that one with the highest
> percentage is selected. Rebates are not stacked!


## Internationalization

If in the project's settings ``USE_I18N = True``, then the rebate's "identifier" is configured
as a translatable field. This requires [django-parler](https://github.com/django-parler/django-parler)
as an additional dependency.
