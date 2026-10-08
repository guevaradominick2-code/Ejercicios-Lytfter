from bubble_sort import bubble_sort as bs
import numpy as np
import pytest

def test_bubble_sort_short_list_acceptance():

    numbers =[11,15,6]

    result = bs(numbers)

    assert result == [6,11,15]


def test_bubble_sort_long_number_list_acceptance():

    number_list = np.random.randint(1, 500, size=105)

    expected_result = np.sort(number_list.copy())

    result = bs(number_list)

    assert np.array_equal(result, expected_result)

def test_bubble_sort_empty_list():

    empty_list = []

    result =bs(empty_list)

    assert result == []

def test_bubble_sort_string_rejection():

    wrong_list = [12,15,16,"Hola"]
    
    with pytest.raises(TypeError):
        bs(wrong_list)