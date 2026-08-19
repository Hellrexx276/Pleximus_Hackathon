import requests


def get_weather(city: str):
    """
    Get the current weather for a city.
    Returns a useful error message instead of crashing
    when the city cannot be found.
    """

    try:

        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(
            url,
            timeout=10
        )

        # Handle unsuccessful HTTP responses
        if response.status_code != 200:
            return {
                "success": False,
                "error": f"Weather information for '{city}' could not be found."
            }

        data = response.json()

        # Make sure the API actually returned weather data
        if (
            "current_condition" not in data
            or not data["current_condition"]
        ):
            return {
                "success": False,
                "error": f"Weather information for '{city}' could not be found."
            }

        current = data["current_condition"][0]

        return {
            "success": True,
            "city": city,
            "temperature_celsius": current["temp_C"],
            "feels_like_celsius": current["FeelsLikeC"],
            "condition": current["weatherDesc"][0]["value"],
            "humidity": current["humidity"],
        }

    except requests.exceptions.RequestException:

        return {
            "success": False,
            "error": (
                f"I couldn't retrieve weather information "
                f"for '{city}' right now."
            )
        }

    except (KeyError, IndexError, ValueError):

        return {
            "success": False,
            "error": (
                f"Weather information for '{city}' "
                f"could not be found."
            )
        }

    except Exception as e:

        return {
            "success": False,
            "error": (
                f"Unable to get weather information "
                f"for '{city}'."
            )
        }