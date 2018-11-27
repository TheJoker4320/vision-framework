import os


def check_import(file_name):
    if file_name == 'modifier.py':
        return False
    elif file_name == 'filter.py':
        return False
    elif file_name == 'publish.py':
        return False
    elif file_name == 'calculation.py':
        return False
    return file_name.endswith('.py') and file_name != '__init__.py'


def create_all(path):
    """

    :param path: the path from which to create the __all__ list
    :type path: string
    :return: list of all modules that end with .py and contain children of modifiers/filter/publish/calculation
    :rtype:
    """
    return [file_name[:-3] for file_name in os.listdir(os.path.dirname(path)) if check_import(file_name)]
