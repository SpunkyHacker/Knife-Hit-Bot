from PIL import Image
import os

# specify the input and output folders
input_folder = "G:\\bots\Knife-Hit-Bot\\negative"
output_folder = "G:\\bots\Knife-Hit-Bot\croped_negative"

# define the crop region as (left, upper, right, lower)
crop_region = (0,1,550,700)

# loop through all the files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # open the image file
        img = Image.open(os.path.join(input_folder, filename))
        
        # crop the image
        cropped_img = img.crop(crop_region)
        
        # save the cropped image to the output folder
        cropped_img.save(os.path.join(output_folder, filename))