import functions_modules

def test_full_sum_for_list():

    numbers = [1,4,5]
    result = functions_modules.summary_list(numbers)
    assert result == 10

def test_invert_string_correctly():

    word = "Hola"
    result = functions_modules.invert_string(word)
    assert result == "aloH"

def test_cases_counter_correctly():

    sentence = "Nice to Meet You"
    result = functions_modules.upper_lower_counter(sentence)
    assert result == (3, 10)