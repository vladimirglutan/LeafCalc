import cv2
import numpy as np
import matplotlib.pyplot as plt

def set_scale(quarter_diameter_pixels):
    """Calculate the scale in pixels per millimeter based on the quarter's diameter in pixels."""
    # Given the standard diameter of a US quarter is 24.26 mm
    quarter_diameter_mm = 24.26
    return quarter_diameter_pixels / quarter_diameter_mm

def calculate_circularity(contour):
    """Calculate the circularity of a contour."""
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    if perimeter == 0:
        return 0
    return 4 * np.pi * area / (perimeter**2)

def identify_quarter(contours):
    """Identify the quarter's contour based on its size and circularity."""
    
    # Filter contours based on area. Adjust min_area and max_area based on your image's resolution.
    min_area = 1000  # Minimum expected area of a quarter in pixels
    max_area = 20000  # Maximum expected area of a quarter in pixels
    potential_quarters = [c for c in contours if min_area < cv2.contourArea(c) < max_area]
    
    if not potential_quarters:
        return None

    # From the potential quarters, select the one with the highest circularity
    quarter_contour = max(potential_quarters, key=calculate_circularity)
    return quarter_contour





def main():
    # Take the image path as input from the user
    image_path = input("Enter the path to the image: ")
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load the image from path: {image_path}")
        return

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Convert the image to grayscale for thresholding and contour detection
    gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Apply morphological closing to merge nearby contours
    kernel = np.ones((5,5), np.uint8)
    binary_closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(binary_closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter out very small contours
    contours = [c for c in contours if cv2.contourArea(c) > 200]  # Adjust the threshold based on your images if needed

    # Identify the quarter's contour
    quarter_contour = identify_quarter(contours)
    if quarter_contour is None:
        print("Couldn't identify the quarter in the image. Ensure it's visible and retry.")
        return
    
    # Calculate the scale using the quarter's diameter
    x, y, w, h = cv2.boundingRect(quarter_contour)
    pixels_per_mm = set_scale(max(w, h))
    
    # Calculate the areas of the leaves
    leaf_contours_corrected = [c for c in contours if c is not quarter_contour]
    leaf_areas_pixels_corrected = [cv2.contourArea(c) for c in leaf_contours_corrected]
    leaf_areas_mm2_corrected = [area_pixels / pixels_per_mm**2 for area_pixels in leaf_areas_pixels_corrected]
    
    # Display the contours on the image
    for index, c in enumerate(leaf_contours_corrected, start=1):
        cv2.drawContours(image_rgb, [c], -1, (0, 255, 0), 2)  # Green for leaves
        M = cv2.moments(c)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
        else:
            cx, cy = 0, 0
        cv2.putText(image_rgb, str(index), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    # Draw the quarter contour in red with increased thickness
    cv2.drawContours(image_rgb, [quarter_contour], -1, (255, 0, 0), 4)

    # Display the image with the drawn contours
    plt.figure(figsize=(10, 10))
    plt.imshow(image_rgb)
    plt.axis('off')
    plt.show()
    
    # Print the areas of the leaves
    for i, area in enumerate(leaf_areas_mm2_corrected, start=1):
        print(f"Leaf {i}: {area:.2f} mm^2")

if __name__ == "__main__":
    main()
