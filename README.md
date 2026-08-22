# Food Health AI

## Research Project

Food Health AI is a research project that investigates whether information
from food product packaging can be used to classify the level of food
processing.

The project focuses on extracting ingredient information from food package
images using Optical Character Recognition (OCR), and then using the
extracted ingredient text for food-processing classification.

The research is based on food products available in Sri Lanka, with
additional publicly available food product data used where appropriate.

---

## Research Question

How effectively can ingredient information extracted from food packaging
images using OCR be used to classify food products according to their level
of processing?

---

## Project Objective

The main objective of this research is to develop and evaluate a method for
extracting ingredient information from food package images and using that
information to classify food products based on their level of processing.

The project will compare different OCR and text-classification approaches
and evaluate their performance using a consistent dataset and evaluation
procedure.

---

## Methodology Overview

The proposed system follows the pipeline below:

Food package image
→ Image preprocessing
→ Ingredient text extraction using OCR
→ Text preprocessing
→ Food-processing classification
→ Final classification

The OCR stage will extract ingredient information from food packaging
images. The extracted text will then be cleaned and prepared for the
classification stage.

Two approaches will be considered for comparison:

- Tesseract as the OCR baseline
- PaddleOCR as the proposed OCR approach

For text classification, a traditional machine-learning approach will be
used as the baseline and compared with a transformer-based classification
approach.

The proposed methodology will be evaluated using appropriate OCR and
classification metrics, stratified cross-validation, and statistical tests.

---

## Dataset

The primary dataset will consist of food product information collected
from food packaging available in Sri Lanka.

The dataset will contain food package images, ingredient-list information,
product metadata, manually verified ingredient text, and the corresponding
classification labels.

Additional publicly available food product information may be used to
supplement the locally collected data. Sources and usage will be documented
in the project documentation.

The complete dataset will not be stored in this GitHub repository because
the image collection may contain a large number of files. A small sample
dataset will be included in the repository for demonstration and
preprocessing purposes.

The complete research dataset will be stored separately and made available
through the project Google Drive link where appropriate.

---

## Dataset Structure

The dataset will contain information such as:

- Product ID
- Product name
- Food category
- Source
- Food package image
- Ingredient-list image
- Ground-truth ingredient text
- Classification label

The dataset will be checked for duplicate products, missing information,
unusable images, and annotation errors before being used in the
experiments.

---

## Current Status

**Milestone 2 — Methodology and Data Description**

At this stage, the project focuses on:

- Defining and documenting the dataset
- Preparing the data collection and annotation procedure
- Defining image and text preprocessing
- Designing the proposed system architecture
- Defining the baseline approaches
- Defining the evaluation and validation strategy
- Preparing the project repository and preprocessing scripts
- Reviewing and updating the research bibliography

Trained models and final experimental results are not included at this
stage, as they are part of the later implementation and experimentation
stages of the project.

---

## Repository Structure

```text
food-health-ai/
│
├── data/
│   ├── sample/
│   │   ├── images/
│   │   └── sample_metadata.csv
│   └── README.md
│
├── src/
│   ├── preprocessing/
│   │   ├── image_preprocessing.py
│   │   └── text_preprocessing.py
│   └── README.md
│
├── docs/
│   ├── methodology.md
│   └── architecture/
│       └── system_architecture.svg
│
├── notebooks/
│   └── README.md
│
├── results/
│   └── README.md
│
├── README.md
├── requirements.txt
└── .gitignore