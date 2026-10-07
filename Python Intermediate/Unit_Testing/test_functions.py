import pytest

from functions_modules import (
    summary_list,
    invert_string,
    upper_lower_counter,
    sentences_ordered,
    number_list,
    prime_number,
    primes_sort
)


# =========================================================
# TESTS PARA summary_list()
# =========================================================

def test_summary_list_positive_numbers():
    numbers = [1, 2, 3, 4, 5]

    result = summary_list(numbers)

    assert result == 15


def test_summary_list_negative_numbers():
    numbers = [-1, -2, -3]

    result = summary_list(numbers)

    assert result == -6


def test_summary_list_mixed_numbers():
    numbers = [-10, 5, 15]

    result = summary_list(numbers)

    assert result == 10


# =========================================================
# TESTS PARA invert_string()
# =========================================================

def test_invert_string_word():
    result = invert_string("Hola")

    assert result == "aloH"


def test_invert_string_phrase():
    result = invert_string("Hola mundo")

    assert result == "odnum aloH"


def test_invert_string_numbers():
    result = invert_string("12345")

    assert result == "54321"


# =========================================================
# TESTS PARA upper_lower_counter()
# =========================================================

def test_upper_lower_counter_mixed():
    result = upper_lower_counter("Hola Mundo")

    assert result == (2, 7)


def test_upper_lower_counter_uppercase():
    result = upper_lower_counter("PYTHON")

    assert result == (6, 0)


def test_upper_lower_counter_lowercase():
    result = upper_lower_counter("python")

    assert result == (0, 6)


# =========================================================
# TESTS PARA sentences_ordered()
# =========================================================

def test_sentences_ordered_three_words():
    result = sentences_ordered("banana-apple-cherry")

    assert result == "apple-banana-cherry"


def test_sentences_ordered_four_words():
    result = sentences_ordered("dog-cat-bird-ant")

    assert result == "ant-bird-cat-dog"


def test_sentences_ordered_already_ordered():
    result = sentences_ordered("apple-banana-cherry")

    assert result == "apple-banana-cherry"


# =========================================================
# TESTS PARA number_list()
# =========================================================

def test_number_list_three_numbers(monkeypatch):

    inputs = iter(["3", "10", "20", "30"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = number_list()

    assert result == [10, 20, 30]


def test_number_list_one_number(monkeypatch):

    inputs = iter(["1", "50"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = number_list()

    assert result == [50]


def test_number_list_negative_numbers(monkeypatch):

    inputs = iter(["3", "-5", "-10", "-15"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = number_list()

    assert result == [-5, -10, -15]


# =========================================================
# TESTS PARA prime_number()
# =========================================================

def test_prime_number_two():
    result = prime_number(2)

    assert result == True


def test_prime_number_seven():
    result = prime_number(7)

    assert result == True


def test_prime_number_thirteen():
    result = prime_number(13)

    assert result == True


# =========================================================
# TESTS PARA primes_sort()
# =========================================================

def test_primes_sort_mixed_numbers():
    numbers = [1, 2, 3, 4, 5, 6]

    result = primes_sort(numbers)

    assert result == [2, 3, 5]


def test_primes_sort_more_numbers():
    numbers = [10, 11, 12, 13, 14, 17]

    result = primes_sort(numbers)

    assert result == [11, 13, 17]


def test_primes_sort_only_primes():
    numbers = [2, 3, 5, 7, 11]

    result = primes_sort(numbers)

    assert result == [2, 3, 5, 7, 11]