# # import numpy as np 
# # # import matplotlib.pyplot as plt
# # # np.random.seed(1)
# # num=10

# # x=np.linspace(0, 1, num)[:, None]

# # print(x)

# # import os 
# # cwd = os.getcwd() 
# # print("Current working directory:", cwd) 


# # import os 
# # path = "C:/Users/odys_/OneDrive/MSc CS/M165 Τεχνολογία ηλ εμποριου/_Εργασία"
# # dir_list = os.listdir(path) 
# # print("Files and directories in '", path, "' :") 
# # print(dir_list) 


# import numpy as np 
# import matplotlib.pyplot as plt
# np.random.seed(1)

# # set the number of samples that we want to create
# num_samples = 3 

# # linspace returns a numpy array of evenly spaced points in the given interval.
# # here we want num_samples points in the interval [0, 10]
# # the [:, None] syntax "adds" a dimension to the vector
# # thus from shape (100,) we get shape (100, 1). This helps with the computations.
# x = np.linspace(0., 10., num_samples)#[:, None]
# print(x)
# print('------------------------')
# print(x.max())
# print('------------------------')
# # generate the responses to the points 
# # we have a linear relationship denoted by the first term and we add some 
# # gaussian(0,1) distributed values to introduce some noise
# # y  = 0.9*x + 0.6*np.random.randn(num_samples, 1)
# # print(y)

# w=np.random.randn(num_samples, 1)
# print(w)

# def buy_pies(num_pies: int, price_per_pie: float) -> str:
#    total_cost = num_pies * price_per_pie
#    return f"Yum! You spent ${total_cost} dollars on {num_pies} pies!"


# # Import Self 
# from typing import Self

# # Define a base class
# class Car:
# 	def set_brand(self,
# 				brand: str) -> Self:
# 		self.brand = brand
# 		return self

# # Define a child class
# class Brand(Car):
# 	def set_speed(self,
# 				speed: float) -> Self:
# 		self.speed = speed
# 		return self

# # Calling object inside print statement
# print(Car().set_brand("Maruti"))
# print(Brand().set_brand("Mar\
# uti").set_speed(110.5))
# print(type(Car().set_brand("Maruti")))
# print(type(Brand().set_brand("Maruti").set_speed(110.5)))
# animal_type = "dog"
# print(f"\nI have a {animal_type}.")

# a="nikos"
# print(f"o {a} einai kala")

# import os 
# cwd = os.getcwd() 
# print("Current working directory:", cwd) 

# path = "D:/ML_LOCAL_WIN/archive"
# dir_list = os.listdir(path) 
# print("Files and directories in '", path, "' :") 
# print(dir_list) 


# # from pathlib import Path
# # Path(r"D:\ML_LOCAL_WIN\archive")

import os
# from PIL import Image
# import numpy as np

# folder = 'D:/ML_LOCAL_WIN/archive/AbdomenCT'
# images = []

# for file_name in os.listdir(folder):
#     if file_name.endswith('.jpeg') or file_name.endswith('.png'):
#         img_path = os.path.join(folder, file_name)
#         img = Image.open(img_path)
#         img = img.resize((128, 128))  # example resize
#         img_array = np.array(img)
#         images.append(img_array)

# images = np.array(images)

# print(images.shape)  # should print (number_of_images, 128, 128, 3) if RGB images
# print(images[0].shape)  # should print (128, 128, 3) if RGB images
# print(images[0].dtype)  # should print the data type of the image array
# print(images)

# def aa (folder):

#     print('------------------------')
#     print(os.listdir(folder))

# foldera = 'D:/ML_LOCAL_WIN'
# aa (foldera)

import os
from PIL import Image
import numpy as np
from sklearn.preprocessing import LabelEncoder

data_dir = 'D:/ML_LOCAL_WIN/archive'  # path to your main image folder

X = []
y = []

# Loop through folders (each folder is a class)
for label in os.listdir(data_dir):
    class_dir = os.path.join(data_dir, label)
    if os.path.isdir(class_dir):
        for file in os.listdir(class_dir):
            if file.endswith('.jpg') or file.endswith('.png'):
                file_path = os.path.join(class_dir, file)
                img = Image.open(file_path)#.convert('L')  # 'L' mode = grayscale
                # img = img.resize((128, 128))  # adjust size as needed
                img_array = np.array(img)
                X=(img_array)
                y=(label)

# Convert to NumPy arrays
X = np.array(X)
y = np.array(y)

# # Add a channel dimension for ML models (e.g., CNNs expect shape: H x W x 1)
# X = X[..., np.newaxis]

# # Encode class labels to integers
# le = LabelEncoder()
# y_encoded = le.fit_transform(y)

print(f"Loaded {img_array.shape[0]} grayscale images with shape {X.shape[1:]}")
