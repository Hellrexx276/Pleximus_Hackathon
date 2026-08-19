def convert_measurement(
    value: float,
    from_unit: str,
    to_unit: str
):
    """
    Convert measurements between common units.
    """

    from_unit = from_unit.lower().strip()
    to_unit = to_unit.lower().strip()

    # Normalize unit names
    aliases = {
        "m": "meters",
        "meter": "meters",
        "meters": "meters",

        "ft": "feet",
        "foot": "feet",
        "feet": "feet",

        "km": "kilometers",
        "kilometer": "kilometers",
        "kilometers": "kilometers",

        "mi": "miles",
        "mile": "miles",
        "miles": "miles",

        "cm": "centimeters",
        "centimeter": "centimeters",
        "centimeters": "centimeters",

        "in": "inches",
        "inch": "inches",
        "inches": "inches",

        "kg": "kilograms",
        "kilogram": "kilograms",
        "kilograms": "kilograms",

        "lb": "pounds",
        "lbs": "pounds",
        "pound": "pounds",
        "pounds": "pounds",

        "c": "celsius",
        "°c": "celsius",
        "celsius": "celsius",

        "f": "fahrenheit",
        "°f": "fahrenheit",
        "fahrenheit": "fahrenheit",
    }

    from_unit = aliases.get(from_unit, from_unit)
    to_unit = aliases.get(to_unit, to_unit)

    # -----------------------------------------------------
    # Length
    # -----------------------------------------------------

    length_to_meters = {
        "meters": 1,
        "feet": 0.3048,
        "kilometers": 1000,
        "miles": 1609.344,
        "centimeters": 0.01,
        "inches": 0.0254,
    }

    if from_unit in length_to_meters and to_unit in length_to_meters:

        meters = value * length_to_meters[from_unit]

        result = meters / length_to_meters[to_unit]

        return {
            "value": value,
            "from_unit": from_unit,
            "to_unit": to_unit,
            "result": result,
        }

    # -----------------------------------------------------
    # Weight
    # -----------------------------------------------------

    weight_to_kg = {
        "kilograms": 1,
        "pounds": 0.45359237,
    }

    if from_unit in weight_to_kg and to_unit in weight_to_kg:

        kilograms = value * weight_to_kg[from_unit]

        result = kilograms / weight_to_kg[to_unit]

        return {
            "value": value,
            "from_unit": from_unit,
            "to_unit": to_unit,
            "result": result,
        }

    # -----------------------------------------------------
    # Temperature
    # -----------------------------------------------------

    if from_unit == "celsius" and to_unit == "fahrenheit":

        result = (value * 9 / 5) + 32

        return {
            "value": value,
            "from_unit": "celsius",
            "to_unit": "fahrenheit",
            "result": result,
        }

    if from_unit == "fahrenheit" and to_unit == "celsius":

        result = (value - 32) * 5 / 9

        return {
            "value": value,
            "from_unit": "fahrenheit",
            "to_unit": "celsius",
            "result": result,
        }

    if from_unit == to_unit:

        return {
            "value": value,
            "from_unit": from_unit,
            "to_unit": to_unit,
            "result": value,
        }

    return {
        "error": (
            f"Cannot convert from '{from_unit}' "
            f"to '{to_unit}'."
        )
    }