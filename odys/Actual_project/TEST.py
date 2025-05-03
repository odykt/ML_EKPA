import os
from PIL import Image

# Define the input directory
input_dir = 'D:/ML_LOCAL_WIN/archive'

# Function to check and resize images to 64x64
def check_and_resize_images(directory, target_size=(64, 64)):
    resized_count = 0  # Counter for resized images
    for category in os.listdir(directory):
        category_path = os.path.join(directory, category)
        if os.path.isdir(category_path):  # Ensure it's a directory
            print(f"Processing folder: {category}")
            for file_name in os.listdir(category_path):
                if file_name.endswith('.jpeg') or file_name.endswith('.png'):  # Check for valid image files
                    img_path = os.path.join(category_path, file_name)
                    try:
                        with Image.open(img_path) as img:
                            if img.size != target_size:  # Check if the image size is not 64x64
                                print(f"Resizing image: {img_path} (Current size: {img.size})")
                                img = img.resize(target_size)  # Resize to 64x64
                                img.save(img_path)  # Save the resized image
                                resized_count += 1  # Increment the counter
                            else:
                                print(f"Image already 64x64: {img_path}")
                    except Exception as e:
                        print(f"Error processing image {img_path}: {e}")
    print(f"Total images resized to {target_size}: {resized_count}")

# Run the function
check_and_resize_images(input_dir)