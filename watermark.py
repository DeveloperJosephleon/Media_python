from PIL import Image, ImageEnhance

# Open the image and the logo
image = Image.open("powder-pic2.jpg")
logo = Image.open("browbyMakelaPNG.png")

# Resize logo to make it larger (adjust size as needed)
logo_width = int(image.width * 0.9)  # 20% of the image width
logo_height = int(logo_width * (logo.height / logo.width))  # Maintain aspect ratio
logo = logo.resize((logo_width, logo_height))

# Adjust transparency
logo = logo.convert("RGBA")
opacity = 128  # Between 0 (transparent) and 255 (opaque)
logo.putalpha(opacity)

# Calculate position for bottom center
position = ((image.width - logo.width) // 2, image.height - logo.height - 150)  # 10px padding from the bottom

# Paste logo onto the image
image.paste(logo, position, logo)

# Save the watermarked image
image.save("watermarked_image2.3.jpg")

print("Watermark added successfully at the bottom center!")
