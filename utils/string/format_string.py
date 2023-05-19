import os


def __get_variable(env_variable, default: str = '') -> str:
    variable = env_variable
    return os.environ.get(variable, default)


def __str_format(variable: str | list | tuple) -> str:
    if not isinstance(variable, str):
        try:
            variable = str(variable)
        except Exception as e:
            print(e, 'Required str format.')
    return str(variable).replace('(', '').replace(')', '')


def format_string_into_list(env_variable: str, default='') -> list:
    formated_string = __str_format(__get_variable(env_variable, default))

    new_list = [
        letter.strip().replace(',', '') for letter in formated_string.split()
    ]
    return new_list
