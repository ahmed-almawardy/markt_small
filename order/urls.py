from django.urls import path
from order import views

app_name = 'order'

urlpatterns = [
    #product
    path('product/create', views.Create.as_view(), name='product-create'),
    path('product/get/<int:pk>', views.Get.as_view(), name='product-get'),
    path('product/list', views.List.as_view(), name='product-list'),
    path('product/update/<int:pk>', views.Update.as_view(), name='product-update'),
    path('product/delete/<int:pk>', views.DeleteOne.as_view(), name='product-delete'),

    #order
    path('order/create', views.CreateOrder.as_view(), name='create'),
    path('order/get/<int:pk>', views.GetOrder.as_view(), name='get'),
    path('order/list', views.ListOrder.as_view(), name='list'),
    path('order/update/<int:pk>', views.UpdateOrder.as_view(), name='update'),
    path('order/delete/<int:pk>', views.DeleteOneOrder.as_view(), name='delete')
]
