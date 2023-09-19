
<pre>
# Leaf Area Calculator

This repository contains a script to calculate the surface area of leaves in an image using a US quarter as a reference for scale.

## Prerequisites

- Python 3
- OpenCV for Python
- NumPy
- Matplotlib

## Setup

1. **Clone the repository**:

\```bash
git clone https://github.com/vladimirglutan/LeafCalc.git
cd LeafCalc
\```

2. **Install the required packages**:

   You can set up a virtual environment if desired:

\```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
\```

   Then, install the packages:

\```bash
pip install opencv-python numpy matplotlib
\```

## Usage

1. **Run the script**:

\```bash
python leaf_calc.py
\```

2. **Input the image path**:

   When prompted, enter the full path to the image you want to analyze.

3. **View the results**:

   The script will display the image with numbered contours around each leaf and the quarter. In the terminal, you'll see the calculated area for each leaf.

## Notes

- Ensure the image has a US quarter for scale.
- The script assumes the quarter is the most circular object in the image.
- Adjust the thresholds in the script if needed, depending on the quality and resolution of your images.
</pre>
