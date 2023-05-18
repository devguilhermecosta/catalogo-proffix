from django.test import TestCase
from django.test import override_settings
from django.urls import reverse, resolve, ResolverMatch
from django.http import HttpResponse
from information import views
from information.tests.base_information import make_information
from information.tests.base_docs import make_doc_obj
import shutil
import contextlib


TEST_DIR = 'test_data'


@override_settings(MEDIA_ROOT=(TEST_DIR + '/docs'))
class InformationTests(TestCase):
    def tearDown(self) -> None:
        with contextlib.suppress(OSError):
            shutil.rmtree(TEST_DIR)
        return super().tearDown()

    def test_contact_url_is_correct(self) -> None:
        url: str = reverse('information:contact')

        self.assertEqual(url, '/contato/')

    def test_contact_url_loads_correct_view(self) -> None:
        response: ResolverMatch = resolve(
            reverse('information:contact')
        )

        self.assertEqual(response.func, views.contact)

    def test_contact_loads_correct_template(self) -> None:
        response: HttpResponse = self.client.get(
            reverse('information:contact')
        )

        self.assertTemplateUsed(response, 'information/pages/contact.html')

    def test_contact_status_code_200(self) -> None:
        response: HttpResponse = self.client.get(
            reverse('information:contact')
        )

        self.assertEqual(response.status_code, 200)

    def test_information_load_correct_data(self) -> None:
        make_information()

        response: HttpResponse = self.client.get(
            reverse('information:contact')
        )
        content: str = response.content.decode('utf-8')

        self.assertIn('descrição da empresa', content)

    def test_information_loads_information_not_available_if_no_information(self) -> None:  # noqa: E501
        response: HttpResponse = self.client.get(
            reverse('information:contact')
        )
        content: str = response.content.decode('utf-8')

        self.assertIn('informações indisponíveis no momento', content)

    def test_information_loads_all_docs(self) -> None:
        doc = make_doc_obj()
        response: HttpResponse = self.client.get(
            reverse('information:contact')
        )
        content: str = response.content.decode('utf-8')

        self.assertIn(doc.afe.name, content)
        self.assertIn(doc.cnpj.name, content)
        self.assertIn(doc.crt.name, content)

    def test_docs_load_docs_not_avaliable_if_not_docs(self) -> None:
        response: HttpResponse = self.client.get(
            reverse('information:contact')
        )
        content: str = response.content.decode('utf-8')

        self.assertIn('documentos não disponíveis', content)

    def test_initial(self) -> None:
        self.fail('testar todo o footer')
