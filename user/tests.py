from django.test import TestCase
from django.urls import reverse_lazy, reverse

from rest_framework.test import APIClient
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)

from user.testHelpers import (NEW_DATA, USER_DATA, create_user)

class UserTest(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user   = create_user()

    def test_user_create(self):
        url = reverse('user:create') 
        data = USER_DATA
        response = self.client.post(data=data, path=url)
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_user_put(self):
        url = reverse_lazy('user:update', args=[self.user.id])
        response = self.client.put(data=NEW_DATA, path=url)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_user_patch(self):
        url = reverse_lazy('user:update', args=[self.user.id]) 
        response = self.client.patch(data=NEW_DATA, path=url)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_user_list(self):
        url = reverse_lazy('user:list') 
        response = self.client.get(path=url) 
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_user_get(self):
        url = reverse_lazy('user:get', args=[self.user.id]) 
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, HTTP_200_OK)
    
    def test_user_delete(self):
        url = reverse_lazy('user:delete', args=[self.user.id]) 
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

    # def test_user_orders(self):
    #     pass
    
    # def test_user_create_order(self):
    #     pass
    
    # def test_user_delete_order(self):
    #     pass
