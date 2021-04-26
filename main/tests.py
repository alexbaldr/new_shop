from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from authorization.models import User

# class BookTestCase(TestCase):

#     def setUp(self):
#         # создайте нового пользователя, отправив запрос к конечной точке 
#         self.user = self.client.post('/user/create/', 
#         data={'first_name':'nemario', 'last_name':'lozario', 
#         'email':'nemario@post.com','password':'i-keep-jumping', 
#         'is_staff':True, 'is_superuser':True})
#         # получить веб-токен JSON для вновь созданного пользователя
#         response = self.client.post('/token/', data={'email':'nemario@post.com','password':'i-keep-jumping'})
#         print(response.data)
#         self.token = response.data['access']
#         self.api_authentication()

#     def api_authentication(self):
#         self.client = APIClient()
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)
    
#     def test_create_author(self):
#         user = User.objects.get(id=1)
#         print(user.is_staff, user.email)
#         data = {'name':'Me', 'country':'US', 'bio':'123456', 'slug':'me'}
#         response = self.client.post('/authors/', data)
#         print(response.data)
#         self.assertEqual(response.status_code,status.HTTP_200_OK)

    # def test_create_book(self):
    #     data = {'name':"New_book",}
    #     response = self.client.post(reverse('book_create'), data)

