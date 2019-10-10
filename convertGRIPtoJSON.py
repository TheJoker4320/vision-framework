import json
from collections import OrderedDict
from bs4.element import NavigableString  # bs4.element.NavigableString
from bs4 import BeautifulSoup


def iter_values(value, returned_list: list) -> list:
    """
    Get all iter values (if there are) and add them to the given list
    No need to return the list, lists are by reference
    """
    if type(value) != NavigableString:
        for iter_value in value:
            iter_values(iter_value, returned_list)
    else:
        returned_list.append(value)


def find_values(bs_xml: BeautifulSoup) -> dict:
    """Search for Values in GRIP file and Match to their Name"""
    returned_dic = {}
    for step in bs_xml.steps.find_all('grip:step'):
        # Check if there is any values
        if step.value is not None:
            returned_dic[step['name']] = []
            for value in step.find_all('value'):
                # Check if there is any iter values
                iter_values(value, returned_dic[step['name']])
    return returned_dic


def clean_dict(dic: dict) -> dict:
    """
    Because of the file format, some enters(\n) are being considered as values
    The function as well replace all spaces(' ') in the key names with underlines ('_')
    """
    new_dic = {}
    for key, value in dic.items():
        key = key.replace(' ', '_')
        value = list(filter(lambda a: a != '\n', value))
        new_dic[key] = value
    return new_dic


def edit_json(json_file_name: str, modifiers: dict):
    """
    Change Values in the modifiers according to the given dictionary
    Note: Change ONLY the given modifiers, the rest will STAY as is
    """
    with open(json_file_name, "r") as file_handler:
        data = json.load(file_handler, object_pairs_hook=OrderedDict)
    # Run-on all the modifiers functions according to their names
    for m in modifiers:
        try:
            data = eval(f'{m}({data})')
        except Exception:
            print(f'{m}: ' + str(NameError("modifier function's name is incorrect or invalid JSON file")))
            # raise NameError("modifier function's name is incorrect or invalid JSON file")
            continue

    # Write back to the JSON file
    with open(json_file_name, 'w') as jf:
        json.dump(data, jf)


def name(opened_json_file: OrderedDict):
    """
    Example for adding a new modifier
    name = name of modifier as in the GRIP file with '_' instead of ' '
    json_file = the opened JSON file (as in the builtin function)
    """
    return opened_json_file


def Resize_Image(opened_json_file: OrderedDict):
    """Change the Resize_Image Values in the JSON data"""
    # Not found on our Modifiers but can be added
    return opened_json_file


def Blur(opened_json_file: OrderedDict):
    """Change the Blur Values in the JSON data"""
    # We have different system so we need to convert this value
    return opened_json_file


def HSV_Threshold(opened_json_file: OrderedDict):
    """Change the HSV_Threshold Values in the JSON data"""
    return opened_json_file


# def Find_Contours(opened_json_file: OrderedDict): # Not supported in GRIP (yet I suppose)
#    return opened_json_files


if __name__ == '__main__':
    # Open GRIP file as a string
    with open('f.grip', 'rb') as gf:
        xml_data = gf.read()
    # Convert the xml string to BeautifulSoup object
    xml = BeautifulSoup(xml_data)
    # Get dict of all values and name
    values = find_values(xml)
    # Clean and formatting the dictionary
    values = clean_dict(values)
    # print(values)
    json_file = 'vision-framework\\examples\\example_try.json'
    # Run on all the modifiers and Change in the JSON file
    edit_json(json_file, values)
