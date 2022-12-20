from django.test import TestCase
from . import models as application_models


class PostTestCase(TestCase):
    def setUp(self):
        self.post = application_models.Post.objects.create(title="Django", author="Django", description="Django")

    def test_post_model(self):
        d = self.post
        self.assertTrue(isinstance(d, application_models.Post))
        self.assertEqual(str(d), 'django')
