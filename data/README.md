# Dataset

This directory contains the sample dataset used for the Food Health AI
research project.

The project dataset consists of food product information collected from
food packaging available in Sri Lanka. The data is used to investigate
whether ingredient information extracted from food package images can be
used to classify the level of food processing.

## Dataset Contents

Each product in the dataset is assigned a unique product ID.

The dataset metadata contains the following information:

- `product_id` - Unique identifier assigned to each product
- `product_name` - Name of the food product
- `category` - Food category of the product
- `brand` - Product brand
- `source` - Source from which the product was collected
- `image_filename` - Filename of the food package image
- `ingredient_image_filename` - Filename of the ingredient-list image
- `ground_truth_ingredient_text` - Manually checked ingredient text
- `nova_label` - Food-processing classification label
- `notes` - Additional information about the product or annotation

## Sample Dataset

A small sample of the dataset is included in this repository under:

```text
data/sample/
├── images/
└── sample_metadata.csv