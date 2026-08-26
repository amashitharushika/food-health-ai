import re

def clean_text(text):
    """
    Clean OCR-extracted ingredient text.

    The cleaning process:
    1. Converts text to lowercase
    2. Removes unnecessary whitespace
    3. Removes unwanted special characters
    4. Keeps letters, numbers and basic punctuation

    Args:
        text (str): OCR-extracted ingredient text.

    Returns:
        str: Cleaned text.
    """

    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Convert text to lowercase
    text = text.lower()

    # Replace line breaks and tabs with spaces
    text = re.sub(r"[\r\n\t]+", " ", text)

    # Keep letters, numbers, spaces, commas, brackets and full stops
    text = re.sub(r"[^a-z0-9,\.\(\)\[\]%\- ]", "", text)

    # Remove repeated spaces
    text = re.sub(r"\s+", " ", text)

    # Remove spaces before punctuation
    text = re.sub(r"\s+([,.])", r"\1", text)

    # Remove leading/trailing whitespace
    text = text.strip()

    return text


def normalize_ingredient_text(text):
    """
    Normalize common formatting variations in ingredient text.

    Args:
        text (str): Cleaned ingredient text.

    Returns:
        str: Normalized ingredient text.
    """

    text = clean_text(text)

    # Normalize common separators
    text = re.sub(r"\s*;\s*", ", ", text)

    # Remove duplicate commas
    text = re.sub(r",\s*,+", ", ", text)

    # Remove duplicate spaces again after normalization
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def preprocess_text(text):
    """
    Apply the complete text preprocessing pipeline.

    Args:
        text (str): Raw OCR-extracted ingredient text.

    Returns:
        str: Preprocessed ingredient text.
    """

    return normalize_ingredient_text(text)
