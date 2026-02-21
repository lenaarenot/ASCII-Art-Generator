# ASCII-Art-Generator

A lightweight Streamlit web application that converts images into ASCII art.

The project demonstrates image processing, pixel intensity mapping, and basic UI interaction using Python.

---

## Features

- Upload JPG or PNG images
- Adjustable output width
- Contrast enhancement
- ASCII rendering in browser (monospace optimized)

---

## Technical Approach

The application:

1. Converts the image to grayscale  
2. Applies contrast enhancement  
3. Resizes the image while preserving aspect ratio  
4. Maps pixel intensity values (0–255) to ASCII characters  
5. Renders the result using monospace formatting  

The core conversion logic is separated from the UI for modularity.

---

## Limitations

The current implementation works best with:

- High-contrast images  
- Line art  
- Icons and logos  
- Black and white graphics  

Photographic images may produce less detailed results due to limited tonal compression and the absence of dithering algorithms.

---

## Tech Stack

- Python 3.13  
- Streamlit  
- Pillow  
- NumPy  

---

## How to Run

```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
streamlit run ascii_art.py
