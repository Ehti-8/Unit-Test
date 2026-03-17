def reverse_string(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    return text[::-1]
