from PIL import Image

# Open the image
image = Image.open("filename.jpg")

# Define coordinates
x1, y1 = 100, 50
x2, y2 = 400, 300

# Crop the image
cropped = image.crop((x1, y1, x2, y2))

# Save or show
cropped.save("cropped_image.jpg")