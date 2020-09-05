from django.test import TestCase
from django.urls import reverse
from..forms import ConnexionForm, InscriptionForm


class GeneralHomePageView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'general/home.html')

    def test_get_context(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.context['form']['login'], ConnexionForm)
        self.assertEqual(response.context['form']['join'], InscriptionForm)
