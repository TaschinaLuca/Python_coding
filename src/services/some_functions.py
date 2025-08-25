def Check_if_is_an_integer(element: str) -> bool:
    """
    :param element: a string
    :return: True-> the string has only characters between '0' and '9', False otherwise
    """

    lower_bound_in_ascii = '0'
    upper_bound_in_ascii = '9'

    for index in range(len(element)):
        if element[index] < lower_bound_in_ascii or element[index] > upper_bound_in_ascii:
            return False

    return True

