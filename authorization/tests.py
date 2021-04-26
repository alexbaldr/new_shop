from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from authorization.models import User

class userProfileTestCase(TestCase):

    def setUp(self):
        # создайте нового пользователя, отправив запрос к конечной точке djoser
        self.user = self.client.post('/user/create/', 
                                    data={'first_name':'mario', 'last_name':'lozario', 
                                    'email':'mario@post.com','password':'i-keep-jumping'})
        # получить веб-токен JSON для вновь созданного пользователя
        response = self.client.post('/token/', data={'email':'mario@post.com','password':'i-keep-jumping'})
        self.token = response.data['access']
        self.api_authentication()

    def api_authentication(self):
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)


    def test_userprofile_detail_retrieve(self):
        response = self.client.get(reverse('profile', kwargs={'pk':1}))
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_userprofile_create(self):
        response = self.client.post('/user/create/', data={
                                                        'first_name':'me', 'last_name':'lozario', 
                                                        'email':'bros@post.com','password':'i-keep-jumping'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_userprofile_put(self):
        profile_data = {'email':'mario@post.com','password':'i-keep-jumping','first_name':'new_mario',}
        response = self.client.put(reverse('profile',kwargs={'pk':1}), data=profile_data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_userprofile_delete(self):
        user = User.objects.get(id=1)
        print(user.email)
        response = self.client.delete(reverse('profile', kwargs={'pk':1}))
        print('now is ', response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)       
