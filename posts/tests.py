from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.


class PostModelTest(TestCase):
    """Класс для тестирования модели Post"""


    def setUp(self):
        Post.objects.create(text = "just a test")


    def test_content_text(self):
        """Тестирует содержание поля 'text' """
        post = Post.objects.get(id = 1)
        excepted_object_name = f"{post.text}"
        self.assertEqual(excepted_object_name, "just a test")


class HomePageViewTest(TestCase):
    """Класс для тестирования отображения домашней страницы"""

    def setUp(self):
        Post.objects.create(text = "This is another text")


    def test_view_url_exist_at_proper_location(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
    

    def test_view_url_by_name(self):
        """Тестирует отработку вьюхи при запроси url по имени"""

        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)


    def test_view_uses_correct_template(self):
        """Тестирует отображение верного шаблона"""

        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "posts/home.html")