import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
from pillow_heif import register_heif_opener


register_heif_opener()


def convert_heic_to_jpg(status_label):
    heic_paths = filedialog.askopenfilenames(filetypes=[("HEIC files", "*.heic")])

    if not heic_paths:
        status_label.configure(text="Please select HEIC image files.")
        return

    for heic_path in heic_paths:
        try:
            image = Image.open(heic_path)
            image = image.convert("RGB")

            # output_folder = "output"
            # source_path = os.path.dirname(heic_path)
            # file_name = os.path.basename(heic_path).replace(".heic", ".jpg")
            # output_path = os.path.join(source_path, output_folder, file_name)

            # if not os.path.exists(output_folder):
            #     os.makedirs(output_folder)

            output_path = heic_path.replace(".heic", ".jpg")

            image.save(output_path, "JPEG")

            status_label.configure(
                text=f"Conversion successful! Converted image saved as {output_path}"
            )
        except Exception as e:
            status_label.configure(text=f"Error converting image: {e}")


class HomeScreen(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("HEIC to JPG Converter")

        label = ctk.CTkLabel(
            self, text="Click the button to select HEIC files and convert them to JPG:"
        )
        label.pack(padx=20, pady=20)

        convert_button = ctk.CTkButton(
            self,
            text="Convert HEIC to JPG",
            command=lambda: convert_heic_to_jpg(status_label),
        )
        convert_button.pack(padx=20, pady=5)

        status_label = ctk.CTkLabel(self, text="")
        status_label.pack(padx=20, pady=20)


def main():
    ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme(
        "green"
    )  # Themes: "blue" (standard), "green", "dark-blue"

    app = HomeScreen()
    app.mainloop()


if __name__ == "__main__":
    main()
