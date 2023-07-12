import os
from PIL import Image

directory = 'C:/Users/mousu/Documents/university/3.5 - Year 2022-23/Term 2/CV/Coursework/OwnData/ownDataset/ownTest/images'

for filename in os.listdir(directory):
    if filename.endswith('.jpg'):
        img_path = os.path.join(directory, filename)
        with Image.open(img_path) as img:
            img = img.convert('RGB')
            img.save(img_path[:-3] + 'jpeg')
