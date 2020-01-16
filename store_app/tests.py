from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Product


class StoreAppTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.product = Product.objects.create(
            title='A good title',
            description='Nice body content',
            manufacturer=self.user,
        )

    def test_string_representation(self):
        product = Product(title='A sample title')
        self.assertEqual(str(product), product.title)

    def test_post_content(self):
        self.assertEqual(f'{self.product.title}', 'A good title')
        self.assertEqual(f'{self.product.manufacturer}', 'testuser')
        self.assertEqual(f'{self.product.description}', 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')
