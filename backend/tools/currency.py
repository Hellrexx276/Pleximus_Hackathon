import requests


def convert_currency(
    amount: float,
    from_currency: str,
    to_currency: str,
):
    """
    Convert currency using the Frankfurter API.
    """

    try:

        url = (
            "https://api.frankfurter.app/latest"
            f"?amount={amount}"
            f"&from={from_currency.upper()}"
            f"&to={to_currency.upper()}"
        )

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        target_currency = to_currency.upper()

        return {
            "amount": amount,
            "from_currency": from_currency.upper(),
            "to_currency": target_currency,
            "converted_amount": data["rates"][target_currency],
        }

    except Exception as e:

        return {
            "error": f"Currency conversion failed: {str(e)}"
        }