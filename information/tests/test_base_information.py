from django.test import TestCase
from information.models import Information
from .base_information import make_information


class InformationBaseTest(TestCase):
    def test_make_information_load_correct_data(self) -> None:
        information = make_information()

        self.assertEqual(information.name, 'information name')
        self.assertEqual(information.about, 'descrição da empresa')

    def test_make_information_is_an_information_instance(self) -> None:
        information = make_information()

        self.assertTrue(isinstance(information, Information))
