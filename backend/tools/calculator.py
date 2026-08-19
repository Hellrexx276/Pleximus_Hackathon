def calculator(expression: str):
    """
    Perform a mathematical calculation.
    """

    try:
        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )

        return {
            "expression": expression,
            "result": result
        }

    except Exception as e:

        return {
            "error": "Invalid mathematical expression"
        }