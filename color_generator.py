#The website i was using showed proper colors but didnt render right in MSTeams. Wrote this to try instead


# Specify the color you want (R, G, B)
color = (173, 216, 230)  # This is light blue

from PIL import Image

# Function to create a GIF with a specific color
def create_gif(color):
    # Create an image with one pixel of the specified color
    img = Image.new('RGB', (1, 1), color=color)
    # Save the image as a GIF file
    img.save('single_pixel.gif', 'GIF')



# Create the GIF with the chosen color
create_gif(color)

# Open the created GIF file and encode it in base64
with open('single_pixel.gif', 'rb') as f:
    gif_data = f.read()

import base64
gif_base64 = base64.b64encode(gif_data).decode('utf-8')

# Print the data URL, which can be used in a browser to display the GIF
data_url = f'data:image/gif;base64,{gif_base64}'
print(data_url)
