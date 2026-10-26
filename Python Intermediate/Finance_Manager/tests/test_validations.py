from datetime import (
    date,
    timedelta
)

import pytest

from validations import (
    validate_amount,
    validate_date
)


def test_validate_date_valid():

    result = validate_date(
        "08/10/2026"
    )

    assert result == date(
        2026,
        10,
        8
    )


def test_validate_date_invalid_format():

    with pytest.raises(
        ValueError,
        match="Formato de fecha inválido"
    ):

        validate_date(
            "2026-10-08"
        )


def test_validate_date_future():

    future = (
        date.today()
        + timedelta(days=1)
    ).strftime(
        "%d/%m/%Y"
    )

    with pytest.raises(
        ValueError,
        match="Future dates"
    ):

        validate_date(
            future
        )


def test_validate_amount_invalid_text():

    with pytest.raises(
        ValueError,
        match="Invalid amount"
    ):

        validate_amount(
            "hello"
        )


def test_validate_amount_positive_number():

    assert (
        validate_amount(
            "2500.50"
        )
        == 2500.50
    )