import numpy as np

from python_project_template import convert_list_to_array


def test_convert_list_to_array():
    list_to_convert = [1,2,3,4,5]
    expected_result = np.array(list_to_convert)
    list_array = convert_list_to_array(list_to_convert)

    # Assert list values are equal before and after conversion
    np.testing.assert_equal(list_array, expected_result)
    # Assert type
    assert isinstance(list_array, np.ndarray)
