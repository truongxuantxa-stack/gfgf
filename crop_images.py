import sys
from PIL import Image, ImageChops

def trim(im):
    # The background is a light gray. Let's get the color of the top-left pixel
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        # Add a small padding of 10 pixels
        bbox = (max(0, bbox[0]-10), max(0, bbox[1]-10), min(im.size[0], bbox[2]+10), min(im.size[1], bbox[3]+10))
        return im.crop(bbox)
    return im

images = [
    "images/screencapture-localhost-5173-onboarding-2026-07-09-21_34_41.png",
    "images/screencapture-localhost-5173-onboarding-2026-07-09-21_35_01.png",
    "images/screencapture-localhost-5173-onboarding-2026-07-09-21_35_20.png"
]

for img_path in images:
    try:
        im = Image.open(img_path)
        im_cropped = trim(im)
        out_path = img_path.replace(".png", "_cropped.png")
        im_cropped.save(out_path)
        print(f"Cropped {img_path} to {out_path}")
    except Exception as e:
        print(f"Error processing {img_path}: {e}")
