from datetime import datetime, date
import math
import re


def validate_date(value):
    if not isinstance(value, str):
        raise ValueError(
            "Formato de fecha inválido (use dd/mm/yyyy)"
        )

    value = value.strip()

    if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", value):
        raise ValueError(
            "Formato de fecha inválido (use dd/mm/yyyy)"
        )

    try:
        user_date = datetime.strptime(
            value,
            "%d/%m/%Y"
        ).date()

    except ValueError:
        raise ValueError(
            "Formato de fecha inválido (use dd/mm/yyyy)"
        )

    if user_date > date.today():
        raise ValueError(
            "Future dates are not allowed"
        )

    return user_date


def validate_amount(value):
    if isinstance(value, bool):
        raise ValueError(
            "Invalid amount. Please enter a positive number."
        )

    try:
        amount = float(value)

    except (TypeError, ValueError):
        raise ValueError(
            "Invalid amount. Please enter a positive number."
        )

    if not math.isfinite(amount) or amount <= 0:
        raise ValueError(
            "Invalid amount. Please enter a positive number."
        )

    return amount