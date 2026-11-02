import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import shutil


FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".pptx", ".ppt", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv", ".webm"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".java", ".cpp", ".c", ".html", ".css", ".js", ".json", ".sql"],
}


class FileOrganizer:

    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("650x540")
        self.root.resizable(False, False)

        self.folder_path = tk.StringVar()
        self.status_var = tk.StringVar(
            value="Select a folder to get started."
        )

        self.setup_ui()

    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding=25)
        main_frame.pack(fill="both", expand=True)

        ttk.Label(
            main_frame,
            text="File Organizer",
            font=("Segoe UI", 23, "bold")
        ).pack(pady=(0, 5))

        ttk.Label(
            main_frame,
            text="Organize your files into folders automatically.",
            font=("Segoe UI", 10)
        ).pack(pady=(0, 25))

        ttk.Label(
            main_frame,
            text="Select Folder",
            font=("Segoe UI", 11, "bold")
        ).pack(anchor="w")

        folder_frame = ttk.Frame(main_frame)
        folder_frame.pack(fill="x", pady=8)

        ttk.Entry(
            folder_frame,
            textvariable=self.folder_path,
            font=("Segoe UI", 10),
            state="readonly"
        ).pack(side="left", fill="x", expand=True)

        ttk.Button(
            folder_frame,
            text="Browse",
            command=self.select_folder
        ).pack(side="left", padx=(8, 0))

        ttk.Label(
            main_frame,
            text="Supported Categories",
            font=("Segoe UI", 11, "bold")
        ).pack(anchor="w", pady=(15, 8))

        categories_frame = ttk.Frame(main_frame)
        categories_frame.pack(fill="x")

        for category in FILE_CATEGORIES:
            ttk.Label(
                categories_frame,
                text=f"📁 {category}",
                font=("Segoe UI", 10)
            ).pack(anchor="w", pady=2)

        ttk.Label(
            categories_frame,
            text="📁 Others — All unsupported file types",
            font=("Segoe UI", 10)
        ).pack(anchor="w", pady=2)

        ttk.Button(
            main_frame,
            text="Preview Files",
            command=self.preview_files
        ).pack(fill="x", pady=(20, 8), ipady=6)

        ttk.Separator(main_frame).pack(fill="x", pady=8)

        ttk.Label(
            main_frame,
            textvariable=self.status_var,
            font=("Segoe UI", 10),
            wraplength=580
        ).pack(pady=8)

        ttk.Label(
            main_frame,
            text="Tip: Preview your files before moving them.",
            font=("Segoe UI", 9)
        ).pack(pady=(8, 0))

    def select_folder(self):
        folder = filedialog.askdirectory(
            title="Select a folder to organize"
        )

        if folder:
            self.folder_path.set(folder)
            self.status_var.set("Folder selected. Ready to preview.")

    def get_category(self, file_path):
        extension = file_path.suffix.lower()

        for category, extensions in FILE_CATEGORIES.items():
            if extension in extensions:
                return category

        return "Others"

    def get_unique_path(self, destination):
        if not destination.exists():
            return destination

        counter = 1

        while True:
            new_name = (
                f"{destination.stem}_{counter}{destination.suffix}"
            )
            new_path = destination.with_name(new_name)

            if not new_path.exists():
                return new_path

            counter += 1

    def preview_files(self):
        selected_folder = self.folder_path.get()

        if not selected_folder:
            messagebox.showwarning(
                "No Folder Selected",
                "Please select a folder first."
            )
            return

        folder = Path(selected_folder)

        if not folder.is_dir():
            messagebox.showerror(
                "Invalid Folder",
                "The selected folder does not exist."
            )
            return

        files = [
            item for item in folder.iterdir()
            if item.is_file()
        ]

        if not files:
            messagebox.showinfo(
                "No Files Found",
                "There are no files to organize."
            )
            return

        preview_window = tk.Toplevel(self.root)
        preview_window.title("File Organization Preview")
        preview_window.geometry("650x480")
        preview_window.transient(self.root)

        ttk.Label(
            preview_window,
            text="File Organization Preview",
            font=("Segoe UI", 17, "bold")
        ).pack(pady=(15, 5))

        ttk.Label(
            preview_window,
            text=f"{len(files)} files found in the selected folder.",
            font=("Segoe UI", 10)
        ).pack(pady=(0, 12))

        table_frame = ttk.Frame(preview_window, padding=(15, 0))
        table_frame.pack(fill="both", expand=True)

        columns = ("filename", "category")

        tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        tree.heading("filename", text="File Name")
        tree.heading("category", text="Destination Folder")

        tree.column("filename", width=390)
        tree.column("category", width=190)

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=tree.yview
        )

        tree.configure(yscrollcommand=scrollbar.set)

        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for file_path in files:
            category = self.get_category(file_path)

            tree.insert(
                "",
                "end",
                values=(file_path.name, category)
            )

        button_frame = ttk.Frame(preview_window, padding=15)
        button_frame.pack(fill="x")

        ttk.Button(
            button_frame,
            text="Cancel",
            command=preview_window.destroy
        ).pack(side="right", padx=(8, 0))

        ttk.Button(
            button_frame,
            text="Confirm & Organize",
            command=lambda: self.confirm_organization(
                folder, preview_window
            )
        ).pack(side="right")

    def confirm_organization(self, folder, preview_window):
        confirm = messagebox.askyesno(
            "Confirm Organization",
            "Are you sure you want to move these files?"
        )

        if not confirm:
            return

        moved = 0
        failed = 0

        files = [
            item for item in folder.iterdir()
            if item.is_file()
        ]

        for file_path in files:
            try:
                category = self.get_category(file_path)
                destination_folder = folder / category

                destination_folder.mkdir(exist_ok=True)

                destination = destination_folder / file_path.name
                destination = self.get_unique_path(destination)

                shutil.move(str(file_path), str(destination))
                moved += 1

            except OSError:
                failed += 1

        preview_window.destroy()

        self.status_var.set(
            f"Organization complete! Moved: {moved} | Failed: {failed}"
        )

        messagebox.showinfo(
            "Organization Complete",
            f"Successfully organized {moved} files.\n"
            f"Failed: {failed}"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizer(root)
    root.mainloop()