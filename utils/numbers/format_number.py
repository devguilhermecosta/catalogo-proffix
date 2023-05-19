import string


def format_phone_number(number: str) -> str:
    other_symbols = '¨'
    all_numbers_and_symbols = (
        string.punctuation + string.ascii_letters + other_symbols)

    formated_number = number.translate(
        {ord(letter): '' for letter in all_numbers_and_symbols}
    )
    return formated_number
