import requests
import tempfile
import ctypes
import os

def download_and_set_wallpaper(image_url):
    # Download the image
    response = requests.get(image_url)
    
    if response.status_code == 200:
        # Create a temporary file to hold the image
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_file.write(response.content)
            temp_file_path = temp_file.name
            
        print(f"Image downloaded to temporary file: {temp_file_path}")
        
        # Set the downloaded image as the wallpaper
        ctypes.windll.user32.SystemParametersInfoW(20, 0, temp_file_path, 3)
        
        # Optionally, delete the temporary file after setting the wallpaper
        os.remove(temp_file_path)

# Example usage:
image_url = 'https://static.ah.nl/static/recepten/img_RAM_PRD171573_612x450_JPG.jpg'  # Replace with the image URL
download_and_set_wallpaper(image_url)
