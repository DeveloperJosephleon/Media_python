from PIL import Image

# Define a list of tuples: [(image_path, logo_path)]
image_logo_pairs = [
    ("powder-pic1.jpg", "browbyMakelaPNG.png"),
    ("powder-pic2.jpg", "browbyMakelaPNG.png"),
    ("powder-pic3.jpg", "browbyMakelaPNG.png"),
    ("powder-pic4.jpg", "browbyMakelaPNG.png"),
    ("powder-pic5.jpg", "browbyMakelaPNG.png"),
    ("powder-pic6.jpg", "browbyMakelaPNG.png"),
]

# Function to add watermark
def add_watermark(image_path, logo_path, output_path):
    # Open the image and the logo
    image = Image.open(image_path)
    logo = Image.open(logo_path)

    # Resize logo to make it proportional to the image
    logo_width = int(image.width * 0.6)  # 20% of the image width
    logo_height = int(logo_width * (logo.height / logo.width))  # Maintain aspect ratio
    logo = logo.resize((logo_width, logo_height))

    # Adjust transparency
    # logo = logo.convert("RGBA")
    # opacity = 128  # Between 0 (transparent) and 255 (opaque)
    # logo.putalpha(opacity)

    # Calculate position for bottom center
    position = ((image.width - logo.width) // 2, image.height - logo.height - 10)  # 10px padding from bottom

    # Paste logo onto the image
    image.paste(logo, position, logo)

    # Save the watermarked image
    image.save(output_path)
    print(f"Watermarked image saved as {output_path}")

# Process each image in the list
for idx, (image_path, logo_path) in enumerate(image_logo_pairs):
    output_path = f"watermarked_image_{idx + 1}.jpg"  # Generate unique output file names
    add_watermark(image_path, logo_path, output_path)
