# Leaf Surface Area Calculator

This repository contains a script to calculate the surface area of leaves in an image using a US quarter as a reference for scale.
Created by Jack Phelps.

## Prerequisites (will be installed below)

- Python 3
- OpenCV for Python
- NumPy
- Matplotlib
- Git


Open your terminal as all commands will be pasted and run there. First, install homebrew and add it to your path. 

``
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
``

When completed, copy the 2 commands under 'next steps' and paste them into the termianl before running them. 


Install python using homebrew: 

``
brew install python
``

``
brew install git
``

## Setup

1. **Clone the repository**:

``
git clone https://github.com/vladimirglutan/LeafCalc.git
``

``
cd LeafCalc
``

2. **Install the required packages**:

``
pip3 install opencv-python numpy matplotlib
``

## Usage

1. **Run the script**:

``
python3 leafcalc.py
``

2. **Input the image path**:

   When prompted, enter the full path to the image you want to analyze. You can find the path of an image by locating it in finder, right clicking, and then while holding the option key, select "copy [your file name] as pathname." You can now paste the path in. Your path should look something like this: /Users/jackphelps/Downloads/image.png. THE IMAGE FILE TYPE MUST BE A PNG. If you are airdropping from an iphone a quick way to do this is take a screenshot of the image on your mac and then rename the screenshot with a .png at the end.
   
4. **View the results**:

   The script will display the image with numbered contours around each leaf and the quarter. In the terminal, you'll see the calculated area for each leaf. Becasue ecah leaf is caclulated indovidually, you can verify and visually check whihc leaf is which.

   <img width="416" alt="Screenshot 2024-05-31 at 2 57 07 PM" src="https://github.com/vladimirglutan/LeafCalc/assets/88109086/d7126ff0-e7f3-4dcc-8062-ec2713a62a1c">

<img width="532" alt="Screenshot 2024-05-31 at 2 58 57 PM" src="https://github.com/vladimirglutan/LeafCalc/assets/88109086/418e6ec3-3a05-4a79-88ce-6659ef2ec064">

## Notes

- Ensure the image has a US quarter for scale.
- The script assumes the quarter is the most circular object in the image.
- Adjust the thresholds in the script if needed, depending on the quality and resolution of your images.
- Thank you Colin for inspiring this project
