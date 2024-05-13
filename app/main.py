from threading import Thread
import customtkinter as ctk
from tkinter import filedialog
from converter import heic_to_jpg


class HomeScreen(ctk.CTk):
    result_var = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title("HEIC to JPG Converter")

        main_frame = ctk.CTkFrame(self)
        main_frame.pack(padx=40, pady=40, expand=True)

        result = "Please select HEIC image files."
        self.result_var = ctk.StringVar(value=result)

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
        self.set_running_state()
        thread = Thread(target=self.conversion_thread)
        thread.start()

    def conversion_thread(self):
        heic_paths = filedialog.askopenfilenames(filetypes=[("HEIC files", "*.heic")])
        result = heic_to_jpg(heic_paths)
        self.set_ready_state(result)

    def set_running_state(self):
        self.convert_button.configure(state="disabled")
        self.status_label.configure(text="Status: RUNNING...")
        self.status_progressbar.start()

    def set_ready_state(self, result):
        self.convert_button.configure(state="normal")
        self.status_label.configure(text="Status: Ready")
        self.status_progressbar.stop()

        self.result_var.set(result)
        self.result_label.configure(width=len(result) * 7)


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
