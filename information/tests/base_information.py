from information.models import Information


def make_information() -> Information:
    information_data: dict = {
        'name': 'information name',
        'phone': '123456',
        'fax': '654321',
        'email': 'email@email.com',
        'about': 'descrição da empresa',
    }

    new_information = Information.objects.create(**information_data)

    return new_information
