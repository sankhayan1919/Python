from PIL import Image
def image_resolution(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return width, height
    except Exception as e:
        return f"Error: {e}"
image_path = 'pic6_img.jpg'
resolution = image_resolution(image_path)
if isinstance(resolution, tuple):
    print(f"The resolution of the image is: {resolution[0]} x {resolution[1]} pixels")
else:
    print(resolution)
