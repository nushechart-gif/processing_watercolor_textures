from pathlib import Path


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