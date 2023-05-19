from django.test import TestCase
from django.test import override_settings
from .base_docs import make_doc_obj
import shutil
import contextlib


TEST_DIR = 'test_data'


@override_settings(MEDIA_ROOT=(TEST_DIR + '/docs'))
class DocsTests(TestCase):
    def tearDown(self) -> None:
        with contextlib.suppress(OSError):
            shutil.rmtree(TEST_DIR)

    def test_make_doc_obj_create_a_instance_of_doc(self) -> None:
        doc = make_doc_obj()
        self.assertEqual(doc.company.name, 'information name')
        self.assertEqual(doc.afe.name, 'docs/afe')
        self.assertEqual(doc.cnpj.name, 'docs/cnpj')
        self.assertEqual(doc.crt.name, 'docs/crt')
