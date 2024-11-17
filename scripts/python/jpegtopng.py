import os
from PIL import Image

# Change the working directory to the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

# Get the list of all files in the current directory
files = os.listdir()

# Loop through each file in the directory
for file_name in files:
    # Check if the file is a JPEG file
    if file_name.lower().endswith('.jpg') or file_name.lower().endswith('.jpeg'):
        try:
            # Open the image using PIL
            img = Image.open(file_name)
            
            # Convert the file name to PNG format
            png_file_name = file_name.rsplit('.', 1)[0] + '.png'
            
            # Save the image in PNG format
            img.save(png_file_name, 'PNG')
            
            # Close the image file
            img.close()
            
            # Delete the original JPEG file
            os.remove(file_name)
            
            print(f"Converted and deleted: {file_name}")
        except Exception as e:
            print(f"Failed to convert {file_name}: {e}")

print("Process complete.")
input()
