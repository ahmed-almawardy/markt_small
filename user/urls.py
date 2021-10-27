from django.urls import path
from user import views

app_name = 'user'
urlpatterns = [
    path('create', views.Create.as_view(), name='create'),
    path('get/<int:pk>', views.Get.as_view(), name='get'),
    path('list', views.List.as_view(), name='list'),
    path('update/<int:pk>', views.Update.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteOne.as_view(), name='delete')
]
