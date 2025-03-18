from PIL import Image

# Load the image
image = Image.open("24039.jpg")

# Resize the image
width, height = image.size
aspect_ratio = height / width
new_width = 100
new_height = int(aspect_ratio * new_width * 0.55)
image = image.resize((new_width, new_height))

# Convert the image to grayscale
image = image.convert("L")

# Define ASCII characters (from darkest to lightest)
ascii_chars = "@%#*+=-:. "

# Convert pixels to ASCII
ascii_art = ""
for y in range(new_height):
    for x in range(new_width):
        pixel = image.getpixel((x, y))
        # Map pixel value (0-255) to ASCII character index (0-9)
        ascii_index = min(pixel // 25, len(ascii_chars) - 1)
        ascii_art += ascii_chars[ascii_index]
    ascii_art += "\n"

# Print the ASCII art
print(ascii_art)