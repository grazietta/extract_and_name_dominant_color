import pandas as pd
import numpy as np
from colorthief import ColorThief

def get_dominant_color(image_name):
    color_thief = ColorThief(image_name)
    dominant_color = color_thief.get_color(quality=1)
    return dominant_color

def remove_hash(data):
    data = data
    return data[1:]

def convert_to_hex(hex_str):
    hex_int = int(hex_str, 16)
    return hex_int

def euclidean_distance(input_color):
    array_color = np.array((convert_to_hex(input_color[0:2]),\
    convert_to_hex(input_color[2:4]),convert_to_hex(input_color[4:])))
    min_dist = float("inf")
    col = dataset.iloc[:,1]
    index = 0
    for color in col:
        array_test = np.array((convert_to_hex(color[0:2])\
        ,convert_to_hex(color[2:4]),convert_to_hex(color[4:])))
        dist = np.linalg.norm(array_test-array_color)
        if dist < min_dist:
            min_color = color
            min_dist = dist
            pos = index
        index = index+1
    return pos
        
def import_dataset(dataset_name):
    dataset = pd.read_csv(dataset_name,header= None)
    dataset.iloc[:,1] = dataset.iloc[:,1].apply(lambda x: remove_hash(x))
    return dataset

def convert_int_color_to_hex(dominant_color):
    r,g,b = rgb_im[0], rgb_im[1], rgb_im[2]
    r,g,b = hex(r)[2:].zfill(2),hex(g)[2:].zfill(2),hex(b)[2:].zfill(2)
    return str(r+g+b)

#fetch dominant color from image
rgb_im = get_dominant_color('images/mineral.jpg')

#convert the the list returned to hex values
input_color = convert_int_color_to_hex(dominant_color)

dataset = import_dataset("rgb.csv")

#find the postion of the closest mathcing color in the dataset
pos = euclidean_distance(input_color)

print("The color of the image is: " + dataset.iloc[pos,0])














