import os


def check_import(file_name):
    if file_name != 'modifier.py':
        return False
    if file_name != 'filter.py':
        return False
    if file_name != 'publish.py':
        return False
    if file_name != 'calculation.py':
        return False
    return file_name.endswith('.py') and file_name != '__init__.py'


def create_all():
    return [file_name[:-3] for file_name in os.listdir(os.path.dirname(__file__)) if check_import(file_name)]
