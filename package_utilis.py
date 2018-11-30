import os


def check_import(file_name):
    """
    Checks if the filename is a python file and is suitable return True if so.
    :param file_name: A name of a file
    :return: True or false
    :rtype boolean
    """
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
    Gets the current files directory and cheacks if they are suitable returns a list of all the names
    :param path: the path from which to create the __all__ list
    :type path: string
    :return: list of all modules that end with .py and contain children of modifiers/filter/publish/calculation
    :rtype: list
    """
    return [file_name[:-3] for file_name in os.listdir(os.path.dirname(path)) if check_import(file_name)]
