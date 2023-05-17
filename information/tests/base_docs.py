from information.models import Docs
from django.core.files.uploadedfile import SimpleUploadedFile
from information.tests.base_information import make_information


def __make_simple_file(name, content):
    file = SimpleUploadedFile(
        name=name,
        content=b'{content}',
    )
    return file


def make_doc_obj() -> Docs:
    doc_info: dict = {
        'company': make_information(),
        'afe': __make_simple_file('afe', 'content'),
        'cnpj': __make_simple_file('cnpj', 'content'),
        'crt': __make_simple_file('crt', 'content'),
    }
    new_doc = Docs.objects.create(**doc_info)

    return new_doc
