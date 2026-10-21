from datetime import datetime, date
def validate_date(value):
    if not isinstance(value, str):
        raise ValueError("Date is not in string format")

    user_date = datetime.strptime(value, "%d/%m/%Y").date()
    today = date.today()

    if not user_date <= today:
        raise ValueError ("Future dates are not allowed")

    return user_date