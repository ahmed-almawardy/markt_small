from django.conf import settings

def price_float(price):
    return float(price)

def format_price(price):
    return f"{price_float(price):{settings.PRICE_FORMAT}}"