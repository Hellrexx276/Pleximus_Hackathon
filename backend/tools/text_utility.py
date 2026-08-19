def text_utility(
    text: str,
    operation: str,
    search_word: str = ""
):
    """
    Perform local text/string operations.
    """

    operation = operation.lower().strip()

    # -----------------------------------------------------
    # Word count
    # -----------------------------------------------------

    if operation == "word_count":

        words = text.split()

        return {
            "operation": operation,
            "word_count": len(words)
        }

    # -----------------------------------------------------
    # Character count
    # -----------------------------------------------------

    elif operation == "character_count":

        return {
            "operation": operation,
            "character_count": len(text)
        }

    # -----------------------------------------------------
    # Character count without spaces
    # -----------------------------------------------------

    elif operation == "character_count_no_spaces":

        count = len(
            text.replace(" ", "")
        )

        return {
            "operation": operation,
            "character_count": count
        }

    # -----------------------------------------------------
    # Uppercase
    # -----------------------------------------------------

    elif operation == "uppercase":

        return {
            "operation": operation,
            "result": text.upper()
        }

    # -----------------------------------------------------
    # Lowercase
    # -----------------------------------------------------

    elif operation == "lowercase":

        return {
            "operation": operation,
            "result": text.lower()
        }

    # -----------------------------------------------------
    # Reverse
    # -----------------------------------------------------

    elif operation == "reverse":

        return {
            "operation": operation,
            "result": text[::-1]
        }

    # -----------------------------------------------------
    # Remove extra spaces
    # -----------------------------------------------------

    elif operation == "remove_extra_spaces":

        result = " ".join(text.split())

        return {
            "operation": operation,
            "result": result
        }

    # -----------------------------------------------------
    # Count a specific word
    # -----------------------------------------------------

    elif operation == "count_word":

        if not search_word:

            return {
                "error": (
                    "search_word is required "
                    "for count_word operation."
                )
            }

        words = text.lower().split()

        count = words.count(
            search_word.lower()
        )

        return {
            "operation": operation,
            "word": search_word,
            "count": count
        }

    # -----------------------------------------------------
    # Palindrome
    # -----------------------------------------------------

    elif operation == "palindrome":

        cleaned = "".join(
            character.lower()
            for character in text
            if character.isalnum()
        )

        is_palindrome = (
            cleaned == cleaned[::-1]
        )

        return {
            "operation": operation,
            "is_palindrome": is_palindrome
        }

    # -----------------------------------------------------
    # Unsupported operation
    # -----------------------------------------------------

    return {
        "error": (
            f"Unsupported text operation: {operation}"
        )
    }