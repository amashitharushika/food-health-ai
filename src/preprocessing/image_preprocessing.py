import cv2
import numpy as np


def load_image(image_path):
    """
    Load an image from the given file path.

    Args:
        image_path (str): Path to the image.

    Returns:
        numpy.ndarray: Loaded image.
    """
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(f"Could not load image: {image_path}")

    return image


def resize_image(image, max_dimension=1280):
    """
    Resize an image so its largest side does not exceed max_dimension,
    keeping aspect ratio. Images already smaller than max_dimension are
    left unchanged, so this only ever downscales, never upscales.

    Args:
        image (numpy.ndarray): Input image.
        max_dimension (int): Maximum allowed size for the longer side.

    Returns:
        numpy.ndarray: Resized image.
    """
    height, width = image.shape[:2]
    longest_side = max(height, width)

    if longest_side <= max_dimension:
        return image

    scale = max_dimension / longest_side
    new_width = int(width * scale)
    new_height = int(height * scale)

    return cv2.resize(
        image,
        (new_width, new_height),
        interpolation=cv2.INTER_AREA
    )

def convert_to_grayscale(image):
    """
    Convert an image from BGR to grayscale.

    Args:
        image (numpy.ndarray): Input image.

    Returns:
        numpy.ndarray: Grayscale image.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def apply_threshold(image):
    """
    Apply Otsu thresholding to improve text visibility.

    Args:
        image (numpy.ndarray): Grayscale image.

    Returns:
        numpy.ndarray: Thresholded image.
    """
    _, thresholded = cv2.threshold(
        image,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return thresholded


def preprocess_image(image_path):
    """
    Apply the basic image preprocessing pipeline.

    The current pipeline:
    1. Load image
    2. Resize image
    3. Convert to grayscale
    4. Apply thresholding

    Args:
        image_path (str): Path to the input image.

    Returns:
        numpy.ndarray: Preprocessed image.
    """
    image = load_image(image_path)
    image = resize_image(image)
    image = convert_to_grayscale(image)
    image = apply_threshold(image)

    return image