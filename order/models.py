from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Sum, Count
from rest_framework.exceptions import APIException
from django.conf import settings

from order.common import format_price


class Product(models.Model):
    name = models.CharField(_("name"), unique=True, max_length=150)
    price = models.CharField(_("price"), max_length=20)
    img = models.ImageField(_("img"), null=True, blank=True)
    desc = models.CharField(_("desc"), max_length=50, null=True, blank=True)

    def price_to_float(self):
        return float(self.price)

    def save(self, **kwargs) -> None:
        self.validate_price()
        return super().save(**kwargs)

    def validate_price(self):
        if not self.price_to_float():
            raise APIException('price cannot be empty')

    def __str__(self):
        return self.name


class Order(models.Model):
    title    = models.CharField(_("name"), max_length=150)
    # price    = models.CharField(_("price"), max_length=20)
    user     = models.ForeignKey("user.User", verbose_name=_("user"), on_delete=models.CASCADE)
    address  = models.CharField(_("desc"), max_length=50, null=True, blank=True)
    products = models.ManyToManyField("Product", verbose_name=_("products"))

    #TODO::Refactor
    @property
    def price(self):
        return self._format_price(self._calculate_price())

    def _calculate_price(self):
        total_price = sum([float(pr.price) for pr in self.products.all()])
        return total_price
    
    def _format_price(self, price):
        return  format_price(price)

    def calculate_products_no(self):
        return self.products.aggregate(no=Count('id'))['no']

    def __str__(self):
       return self.title


class ProductsOrder(models.Model):
    product  = models.ForeignKey("Product", verbose_name=_("product"), on_delete=models.CASCADE)
    order    = models.ForeignKey("Order", verbose_name=_("order"), on_delete=models.CASCADE)
    quantity = models.IntegerField(_("quantity"), default=1)

    def __str__(self):
        return f'{self.product}:{self.order}'