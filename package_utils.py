import os

black_list = ['modifier.py', 'extractor.py' 'filter.py', 'publish.py', 'calculation.py', '__init__.py']


def check_import(file_name):
    """
    Checks if the filename is a python file and is suitable return True if so.
    :param file_name: A name of a file
    :return: True or false
    :rtype boolean
    """
    if file_name in black_list:
        return False
    return file_name.endswith('.py')


def create_all(path):
    """
    Gets the current files directory and checks if they are suitable returns a list of all the names
    :param path: The path from which to create the __all__ list
    :type path: string
    :return: A list of all modules that end with .py and contain children of modifiers/extractors/filter
    /publish/calculation
    :rtype: list
    """
    return [file_name[:-3] for file_name in os.listdir(os.path.dirname(path)) if check_import(file_name)]
