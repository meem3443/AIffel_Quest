import matplotlib as mpl
import matplotlib.pyplot as plt
from PIL import Image, ImageColor
import os
import numpy as np
img_path = "/Users/breadd123456/Code_project/Python/Aiffel_Quest_KJS/AIffel_Quest/Study/numpys/image/NewYork.png"
img = Image.open(img_path)
print(img_path)
print(type(img))

#plt.imshow(img)
#plt.axis('off')  # Hide axes
#plt.show()  # Display the image

#print(img.size)
W, H = img.size
print((W, H))

print(img.format)
print(img.size)
print(img.mode)


img = img.crop((30,30,100,100))
#plt.imshow(img)
#plt.axis('off')  # Hide axes
#plt.show()  # Display the image

cropped_img_path = "/Users/breadd123456/Code_project/Python/Aiffel_Quest_KJS/AIffel_Quest/Study/numpys/image/croped_img.png"
img.save(cropped_img_path)

img_arr = np.array(img)
print(type(img))
print(type(img_arr))
print(img_arr.shape)
print(img_arr.ndim)
print(img_arr)

img_g = Image.open(img_path).convert('L')
plt.imshow(img_g)
plt.show()

img_g_arr = np.array(img_g)
print(type(img_g_arr))
print(img_g_arr.shape)
print(img_g_arr.ndim)
print(img_g_arr)


red = ImageColor.getcolor('RED','RGB')
reda = ImageColor.getcolor('red','RGBA')
yellow = ImageColor.getcolor('yellow','RGB')
print(red)
print(reda)
print(yellow)