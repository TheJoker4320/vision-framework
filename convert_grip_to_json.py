import json
import sys
from collections import OrderedDict
from bs4.element import NavigableString
from bs4 import BeautifulSoup


def iter_values_element_finder(value_element: NavigableString, returned_list: list):
    """
    Get all iter values (if there are) and add them to the given list
    NOTE: No need to return the list, lists are by reference

    :param value_element: the value of the step in the xml of beautifulsoup
    :type value_element: NavigableString

    :param returned_list: the list of all the values of the given step
    :type returned_list: list

    """
    # The wanted type is NavigableString, because it can be several types there is a check
    if type(value_element) != NavigableString:
        # Go all the way util it is NavigableString (if there are none there will be no values)
        for iter_value in value_element:
            iter_values_element_finder(iter_value, returned_list)
    # If it is NavigableString add it's value to the returned_list
    else:
        returned_list.append(value_element)


def find_values(beautifulsoup_xml: BeautifulSoup) -> dict:
    """
    Search for Values in GRIP file and Match to their Name

    :param beautifulsoup_xml: the xml the beautifulsoup created
    :type: beautifulsoup_xml: BeautifulSoup

    :rtype: dict
    """
    returned_dictionary = {}

    # Go over all the steps in the GRIP file
    for step in beautifulsoup_xml.steps.find_all('grip:step'):
        # Check if there is any values
        if step.value is not None:
            returned_dictionary[step['name']] = []
            for value in step.find_all('value'):
                # Check if there is any iter values
                iter_values_element_finder(value, returned_dictionary[step['name']])
    return returned_dictionary


def clean_and_format_dictionary(values_dict: dict) -> dict:
    """
    Because of the file format, some enters(\n) are being considered as values
    The function as well replace all spaces(' ') in the key names with underlines ('_')
    """
    cleaned_dict = {}
    for key, value in values_dict.items():
        key = key.replace(' ', '_')
        value = list(filter(lambda val: val != '\n', value))
        cleaned_dict[key] = value
    return cleaned_dict


def edit_json(json_file_name: str, grip_data: dict):
    """
    Change Values in the JSON according to the given dictionary
    Note: Change ONLY the given values, the rest will STAY as is

    :param json_file_name: the JSON file's name
    :type json_file_name: str

    :param grip_data: the dictionary where the key is the name like in the GRIP and the value is it's values in
                      the GRIP file
    :type grip_data: dict
    """
    # Open the JSON file
    with open(json_file_name, "r") as json_handler:
        properties = json.load(json_handler, object_pairs_hook=OrderedDict)

    # Run-on all the modifiers functions according to their names
    for grip_name, grip_values in grip_data.items():
        try:
            # Call the wanted function to convert the values of the GRIP file to the JSON file
            properties = eval("edit_function(properties, grip_values)", {},
                              {"edit_function": GRIP_NAME_TO_FRAMEWORK_FUNCTIONS[grip_name],
                               "properties": properties, "grip_values": grip_values})
        # If there is an any exception while trying to run print an Exception and continue
        except Exception as exception:
            print(exception.__class__.__name__ + f' {grip_name}: ' + str(
                NameError("the function's name is incorrect (or not in the GRIP_NAME_TO_FRAMEWORK_FUNCTIONS"
                          "dictionary or invalid JSON file")))
            continue

    # Write back to the JSON file
    with open(json_file_name, 'w') as jf:
        json.dump(properties, jf)


"""
This section below used for function that convert the GRIP values to the JSON and return it
after you add the function do not forget to add it to the GRIP_NAME_TO_FRAMEWORK_FUNCTIONS dictionary

you can add your own function by the following format:

def name(opened_json_file: OrderedDict, grip_values: list):
    # Example for adding a new converter function
    # name = the function name
    # json_file = the opened JSON file (as in the builtin function)
    # grip_values = the values read from the GRIP file for this section only

    return opened_json_file

"""


def blur(opened_json_file: OrderedDict, grip_values: list):
    """
    Change the Blur Values in the JSON data

    :param opened_json_file: the given JSON file opened as a OrderedDict
    :type opened_json_file: OrderedDict

    :param grip_values: the inserted values in the GRIP file for this action by order from first to last
    :type grip_values: list

    """

    # We have different system so we need to convert this value
    # our system gets a kernel with multiple values instead of one as in GRIP that is why we convert it
    opened_json_file["modifiers"]["Blur"]["kernel"] = [grip_values[1], grip_values[1]]

    return opened_json_file


def hsv_threshold(opened_json_file: OrderedDict, grip_values: list):
    """
    Change the HSV_Threshold Values in the JSON data

    :param opened_json_file: the given JSON file opened as a OrderedDict
    :type opened_json_file: OrderedDict

    :param grip_values: the inserted values in the GRIP file for this action by order from first to last
    :type grip_values: list

    """

    # Change the Hue (H)
    opened_json_file["modifiers"]["ColorThreshold"]["low_h"] = grip_values[0]
    opened_json_file["modifiers"]["ColorThreshold"]["high_h"] = grip_values[1]

    # Change the Saturation (S)
    opened_json_file["modifiers"]["ColorThreshold"]["low_s"] = grip_values[2]
    opened_json_file["modifiers"]["ColorThreshold"]["high_s"] = grip_values[3]

    # Change the Value (V)
    opened_json_file["modifiers"]["ColorThreshold"]["low_v"] = grip_values[4]
    opened_json_file["modifiers"]["ColorThreshold"]["high_v"] = grip_values[5]

    return opened_json_file


def mask(opened_json_file: OrderedDict, grip_values: list):
    """
    Change the HSV_Threshold (because the mask is in it) Values in the JSON data

    :param opened_json_file: the given JSON file opened as a OrderedDict
    :type opened_json_file: OrderedDict

    :param grip_values: the inserted values in the GRIP file for this action by order from first to last
    :type grip_values: list

    """

    # NOTE: once it is set it can not be change to False
    #       to change it to False you must do it directly through the JSON file
    opened_json_file["modifiers"]["ColorThreshold"]["high_v"] = True
    return opened_json_file


"""
A global dictionary for the integreation from the GRIP naming convention to the wanted function
in the key there is the name as it is in the GRIP (notice the there are '_' instead of ' ')
in the value there is the function you want to use to edit the JSON file (notice that you need to create one above)

see the first example in the dictionary for guidance
"""
GRIP_NAME_TO_FRAMEWORK_FUNCTIONS = {
    "The_Name_In_Grip": "the_function_to_use_for_this_case",
    "Blur": blur,
    "HSV_Threshold": hsv_threshold,
    "Mask": mask
}

if __name__ == '__main__':
    # Check if input files were received correctly
    if not (len(sys.argv) == 3 and sys.argv[1].endswith('.grip') and sys.argv[2].endswith('.json')):
        raise Exception("Need two files (in this order): a GRIP file (.grip) and a JSON file (.json)")

    # Open GRIP file as a string
    with open(sys.argv[1], 'rb') as gf:
        xml_data = gf.read()
    # Convert the xml string to BeautifulSoup object
    xml = BeautifulSoup(xml_data)

    # Get dict of all values and name
    values = find_values(xml)
    # Clean and formatting the dictionary
    values = clean_and_format_dictionary(values)

    json_file = sys.argv[2]

    # Run on all the modifiers and Change in the JSON file
    edit_json(json_file, values)
