from PIL import Image, ImageSequence
import os

def create_gif(input_folder, output_gif, duration=200, loop=0):
    # Get a list of all PNG files in the input folder
    png_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.png')]

    # Sort the files to ensure the correct order
    png_files.sort()

    # Create a list to store each frame
    frames = []

    # Open each PNG image and append it to the frames list
    for png_file in png_files:
        image_path = os.path.join(input_folder, png_file)
        img = Image.open(image_path)
        frames.append(img)

    # Save the frames as a GIF
    frames[0].save(output_gif, save_all=True, append_images=frames[1:], duration=duration, loop=loop)

# Example usage
input_folder = 'fermi acceleration new/Barrier sizes/Black and White Images/125.0'
output_gif = 'fermi acceleration new/GIF/125px.gif'
create_gif(input_folder, output_gif)