

# Importing Image module from PIL package
from PIL import Image


# creating a image object (main image)
im1 = Image.open(r"C:\Users\markw\Pictures\Screenpresso\2023-04-01_09h13_45.png")


im1 = im1.save("2023-04-01_09h13_45.png")
print(im1)
