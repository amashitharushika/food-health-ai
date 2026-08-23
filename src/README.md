# Source Code

This directory contains the source code used for the project.

## preprocessing/

Contains the preprocessing scripts used before the OCR and classification
stages.

### image_preprocessing.py

The image preprocessing stage prepares food package and ingredient-list
images before OCR. The current implementation includes image loading,
resizing, grayscale conversion and thresholding.

The preprocessing steps may be adjusted during later experimentation
depending on their effect on OCR performance.
### text_preprocessing.py

Contains the text preprocessing functions used before classification.