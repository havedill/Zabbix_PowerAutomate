color_list = [ 
    (195, 195, 195), # Not Classified Default / Gray
    (0, 158, 26), # Resolved / Green
    (230, 0, 0), # Dark Red Disaster
    (230, 77, 0), # Orange High
    (230, 131, 0), # Orange Average
    (182, 179, 255), # Light Blue Information
    (238, 201, 83)
] 

descriptions = [
    "Not Classified Default / Gray",
    "Resolved / Green",
    "Dark Red Disaster",
    "Orange High",
    "Orange Average",
    "Light Blue Information",
    "Warning"
]

from PIL import Image
import base64

# Function to create a GIF with a specific color
def create_gif(color, size):
    # Create an image with the specified size
    img = Image.new('RGB', size, color=color)
    # Save the image to a GIF file
    img.save('single_pixel.gif', 'GIF')

# Define the size
size = (8, 1)  # 8x1 image

# Create and encode the GIFs
for color, description in zip(color_list, descriptions):
    create_gif(color, size)

    # Open the GIF file and encode it to base64
    with open('single_pixel.gif', 'rb') as f:
        gif_data = f.read()

    gif_base64 = base64.b64encode(gif_data).decode('utf-8')

    # Print the description and data URL
    data_url = f'data:image/gif;base64,{gif_base64}'
    print(f'{description}: {data_url}')
