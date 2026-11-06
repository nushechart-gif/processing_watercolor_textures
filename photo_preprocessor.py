from pathlib import Path
from PIL import Image

input_folder = Path(r"C:\Users\User\Desktop\текстуры")
output_folder = Path(r"C:\Users\User\Desktop\текстуры\processed")
output_folder.mkdir(exist_ok=True)
jpg_files = list(input_folder.glob("*.jpg"))
heic_files = list(input_folder.glob("*.heic"))
all_images = jpg_files + heic_files
print(f"Найдено JPG: {len(jpg_files)}")
print(f"Найдено HEIC: {len(heic_files)}")
print(f"Всего файлов: {len(all_images)}")
for i, img_path in enumerate(all_images,start=1):
    print(f"texture_{i:02d}.jpg")
first_image_path = all_images[0]
img = Image.open(first_image_path)
width, height = img.size 
print(f"Размер: {width} x {height}")
print(f"Режим: {img.mode}")

left = 200
upper = 200
right = width - 200
lower = height - 200
cropped_img = img.crop((left, upper, right, lower))
cropped_width, cropped_height = cropped_img.size
print(f"Размер после обрезки: {cropped_width} x {cropped_height}")