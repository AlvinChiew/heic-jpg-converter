from threading import Thread
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
from pillow_heif import register_heif_opener


def convert_heic_to_jpg(heic_paths):
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


class HomeScreen(ctk.CTk):
    result_var = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title("HEIC to JPG Converter")

        main_frame = ctk.CTkFrame(self)
        main_frame.pack(padx=40, pady=40, expand=True)

        result = "Please select HEIC image files."
        self.result_var = ctk.StringVar(value=result)
        # result.set("Please select HEIC image files.")

        label = ctk.CTkLabel(
            main_frame,
            text="Click the button to select HEIC files to convert them to JPG:",
        )
        label.pack(pady=(0, 40), expand=True)

        self.convert_button = ctk.CTkButton(
            main_frame,
            text="Convert HEIC to JPG",
            height=50,
            width=200,
            font=("TkDefaultFont", 16),
            command=self.click_convert_btn,
        )
        self.convert_button.pack(pady=(0, 40), expand=True)

        self.status_label = ctk.CTkLabel(main_frame, text="Status: Ready")
        self.status_label.pack(pady=(0, 10), expand=True)
        self.status_progressbar = ctk.CTkProgressBar(
            main_frame, width=120, mode="indeterminate"
        )
        self.status_progressbar.pack(pady=(0, 40), expand=True)

        self.result_label = ctk.CTkEntry(
            main_frame,
            textvariable=self.result_var,
            width=len(result) * 6.5,
            fg_color=self.cget("fg_color"),
            border_color=self.cget("fg_color"),
            state="readonly",
            justify="center",
        )
        self.result_label.pack(pady=(0, 20), expand=True)

    def click_convert_btn(self):
        self.convert_button.configure(state="disabled")
        self.status_label.configure(text="Status: RUNNING...")
        self.status_progressbar.start()

        thread = Thread(target=self.conversion_thread)
        thread.start()

    def conversion_thread(self):
        heic_paths = filedialog.askopenfilenames(filetypes=[("HEIC files", "*.heic")])
        result = convert_heic_to_jpg(heic_paths)
        self.result_var.set(result)
        self.result_label.configure(width=len(result) * 7)

        self.convert_button.configure(state="normal")
        self.status_label.configure(text="Status: Ready")
        self.status_progressbar.stop()


def main():
    ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme(
        "green"
    )  # Themes: "blue" (standard), "green", "dark-blue"
    ctk.set_widget_scaling(1.2)

    app = HomeScreen(fg_color=["gray86", "gray17"])  # transparent
    app.mainloop()


if __name__ == "__main__":
    main()
