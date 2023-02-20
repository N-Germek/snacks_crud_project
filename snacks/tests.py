from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack


class SnackTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass")
        self.snack = Snack.objects.create(
            name='bon bon', purchaser=self.user, description='chocolate ball'
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "bon bon")

    def test_snack_name(self):
        self.assertEqual(f'{self.snack.title}', 'bon bon')

    def test_snack_purchaser(self):
        self.assertEquals(f'{self.snack.purchaser}', self.user)

    def test_snack_description(self):
        self.assertEqual(f'{self.snack.description}', 'chocolate ball')

    def test_snack_list_page_status_code(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_list_page_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "_base.html")

    def test_snack_detail_page_template(self):
        url = reverse("snack_detail")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_detail.html")
        self.assertTemplateUsed(response, "_base.html")

    def test_snack_delete_page_template(self):
        url = reverse("snack_delete")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_delete.html")
        self.assertTemplateUsed(response, "_base.html")

    def test_snack_create_template(self):
        url = reverse("snack_create")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_create.html")
        self.assertTemplateUsed(response, "_base.html")

    def test_snack_update_page_template(self):
        url = reverse("snack_update")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_update.html")
        self.assertTemplateUsed(response, "_base.html")
