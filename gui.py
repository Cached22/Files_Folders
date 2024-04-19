```python
import tkinter as tk
from tkinter import filedialog, messagebox
import json
import threading
from file_processor.py import traverse_directory
from csv_exporter.py import export_to_csv

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('File Summarizer')
        self.geometry('400x300')

        self.create_widgets()

    def create_widgets(self):
        self.directory_label = tk.Label(self, text="Select Directory:")
        self.directory_label.pack()

        self.directory_input = tk.Entry(self, width=50)
        self.directory_input.pack()

        self.browse_button = tk.Button(self, text="Browse", command=self.browse_directory)
        self.browse_button.pack()

        self.start_button = tk.Button(self, text="Start", command=self.start_processing)
        self.start_button.pack()

        self.progress_bar = tk.Label(self, text="", anchor="w")
        self.progress_bar.pack(fill=tk.BOTH, expand=True)

        self.status_label = tk.Label(self, text="Status: Waiting for input...")
        self.status_label.pack()

    def browse_directory(self):
        directory = filedialog.askdirectory()
        self.directory_input.delete(0, tk.END)
        self.directory_input.insert(0, directory)

    def start_processing(self):
        directory = self.directory_input.get()
        if not directory:
            messagebox.showerror("Error", "Please select a directory.")
            return

        self.status_label.config(text="Status: Processing...")
        threading.Thread(target=self.process_directory, args=(directory,), daemon=True).start()

    def process_directory(self, directory):
        try:
            file_list = traverse_directory(directory)
            summaries = []
            for file in file_list:
                summary = generate_summary(file)
                summaries.append(summary)
            export_to_csv(summaries)
            self.status_label.config(text="Status: Completed")
        except Exception as e:
            self.status_label.config(text="Status: Error")
            messagebox.showerror("Error", str(e))

    def update_progress(self, progress):
        self.progress_bar.config(text=progress)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
```