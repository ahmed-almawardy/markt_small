from order.models import (Order, Product)

ORDER_DATA = {
    'products': [1,2,3],
    'user': 1,
    'address':'Cairo',
    'title': 'orderee'
}

ORDER_DATA_NEW = {
    'serial': '12228',
    'products': [1,3],
    'user': 1,
    'address':'Alex',
    'title': 'a title'
}

PRODUCT_DATA = {
    'name':"prodcut",
    'price':"564.50",
    'img':"",
    'desc':"",
}

PRODUCT_DATA_NEW = {
    'name': 'prodcut new',
    'img':'',
    'price': '264.50',
}

def create_order(**update):
    data = ORDER_DATA.copy()
    data.pop('products', [])
    products = update.pop('products', [])
    if update:
        data.update(**update)

    order = Order.objects.create(**data)
    order.products.set(products)
    return order
    
def create_product(**update):
    data = PRODUCT_DATA.copy()
    if update:
        data.update(**update)
    product =  Product.objects.create(**data)
    return product