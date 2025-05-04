import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define the input directory
input_dir = 'D:/ML_LOCAL_WIN/archive'

# Function to create histograms with density plots for pixel values of all images per class
def plot_pixel_histograms_with_density(directory):
    for category in os.listdir(directory):
        category_path = os.path.join(directory, category)
        if os.path.isdir(category_path):  # Ensure it's a directory
            print(f"Processing folder: {category}")
            pixel_values = []  # List to store pixel values for the class
            
            for file_name in os.listdir(category_path):
                if file_name.endswith('.jpeg') or file_name.endswith('.png'):  # Check for valid image files
                    img_path = os.path.join(category_path, file_name)
                    try:
                        with Image.open(img_path) as img:
                            img_array = np.array(img)  # Convert image to NumPy array
                            pixel_values.extend(img_array.flatten())  # Flatten and add pixel values
                    except Exception as e:
                        print(f"Error processing image {img_path}: {e}")
            
            # Plot histogram with density plot for the class
            if pixel_values:
                plt.figure(figsize=(10, 5))
                sns.histplot(pixel_values, bins=256, kde=True, color='blue', stat="density", alpha=0.6)
                plt.title(f"Pixel Value Distribution with Density for Class: {category}")
                plt.xlabel("Pixel Value")
                plt.ylabel("Density")
                plt.grid(axis='y', alpha=0.75)
                plt.show()

# Run the function
plot_pixel_histograms_with_density(input_dir)