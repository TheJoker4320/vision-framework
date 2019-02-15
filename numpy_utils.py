import numpy


def remove(origin_array, delete_array):
    """

    :param origin_array: array to remove from
    :type origin_array:  numpy array
    :param delete_array: array to be removed
    :type delete_array: numpy array
    :return: the original array without the deleted array
    :rtype: numpy array
    """

    origin_array_list = origin_array.tolist()
    origin_array_list.remove(delete_array.tolist())
    return numpy.array(origin_array_list)
