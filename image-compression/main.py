from PIL import Image
import os

def resize_and_compress_image(image, directory):
    img = Image.open(os.path.join(directory, image))
    width = int(input('Enter the width of the image (in pixels): ') or 800)
    height = int((width / float(img.size[0])) * float(img.size[1]))
    img = img.resize((width, height), Image.ANTIALIAS)
    img.save(os.path.join(directory, 'resized_' + image), quality=60, optimize=True)

def search_image_files(directory):
    image_list = [f for f in os.listdir(directory) if f.endswith('.jpg') or f.endswith('.png')]
    return image_list

def main():
    directory = input('Enter the path to the image files: ') or '.'
    image_list = search_image_files(directory)

    if not image_list:
        print("No image files found in the directory. Skipping compression.")
        return

    for image in image_list:
        resize_and_compress_image(image, directory)

if __name__ == '__main__':
    main()