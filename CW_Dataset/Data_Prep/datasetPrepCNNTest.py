import os
import shutil

# Set the paths to the train directory
test_dir = 'C:/Users/mousu/Documents/university/3.5 - Year 2022-23/Term 2/CV/Coursework/CV2023_CW_Dataset/test'
test_new_dir = 'C:/Users/mousu/Documents/university/3.5 - Year 2022-23/Term 2/CV/Coursework/CV2023_CW_Dataset/testNew'

# Create the new train directory and sub-directories
os.makedirs(os.path.join(test_new_dir, '0'), exist_ok=True)
os.makedirs(os.path.join(test_new_dir, '1'), exist_ok=True)
os.makedirs(os.path.join(test_new_dir, '2'), exist_ok=True)

# Loop through the JPEG files in the train/Image directory
jpeg_files = [f for f in os.listdir(os.path.join(test_dir, 'images')) if f.endswith('.jpeg')]
for jpeg_file in jpeg_files:
    label_file = os.path.join(test_dir, 'labels', jpeg_file.split('.')[0] + '.txt')
    
    # Check if the label file exists
    if os.path.exists(label_file):
        with open(label_file, 'r') as f:
            classification = int(f.readline().strip())
            print(f"Copying image {jpeg_file} to label {classification} folder")
            shutil.copy2(os.path.join(test_dir, 'images', jpeg_file), os.path.join(test_new_dir, str(classification), jpeg_file))
    else:
        print(f"Label file not found for image {jpeg_file}")
