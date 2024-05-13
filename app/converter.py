from PIL import Image
from pillow_heif import register_heif_opener


def heic_to_jpg(heic_paths):
    register_heif_opener()
    if not heic_paths:
        return "Please select HEIC image files."

    result = ""
    for heic_path in heic_paths:
        try:
            # time.sleep(5)
            image = Image.open(heic_path)
            image = image.convert("RGB")

            output_path = heic_path.lower().replace(".heic", ".jpg")

            image.save(output_path, "JPEG")

            result = (
                f"Conversion successful! Last converted image saved as {output_path}"
            )

        except Exception as e:
            return f"Error converting image: {e}"

    return result
