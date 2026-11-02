# File Organizer 📁

A simple and user-friendly Python desktop application that automatically organizes files into categorized folders based on their file extensions. The application includes a preview system, file size information, duplicate filename protection, and a live progress bar for a safer and more informative file organization experience.

## ✨ Features

- Browse and select any folder to organize
- Preview files before making any changes
- View each file's destination category before organizing
- Display individual file sizes in the preview
- Display the total number and combined size of selected files
- Automatically organize files into categories
- Supports Images, Documents, Videos, Audio, Archives, and Code files
- Moves unsupported file types into an `Others` folder
- Prevents duplicate filename conflicts by creating unique filenames
- Shows a confirmation before files are moved
- Live progress bar with percentage completion
- Displays real-time moved and failed file counts
- Simple and user-friendly graphical interface built with Tkinter

## 🛠️ Technologies Used

- Python 3.11
- Tkinter
- pathlib
- shutil

## 📋 Requirements

- Python 3.11 or later
- Tkinter

No external Python packages are required.

## 🚀 Installation

Clone the repository:

    git clone https://github.com/RaavanHrishi07/File-Organizer.git

Navigate to the project directory:

    cd File-Organizer

## ▶️ How to Run

Run the following command:

    python main.py

## 📂 Supported Categories

| Category | Supported Formats |
|---|---|
| Images | JPG, JPEG, PNG, GIF, BMP, WEBP, SVG |
| Documents | PDF, DOC, DOCX, TXT, XLSX, XLS, PPTX, PPT, CSV |
| Videos | MP4, MKV, MOV, AVI, WMV, WEBM |
| Audio | MP3, WAV, AAC, FLAC, OGG, M4A |
| Archives | ZIP, RAR, 7Z, TAR, GZ |
| Code | PY, JAVA, CPP, C, HTML, CSS, JS, JSON, SQL |
| Others | All unsupported file types |

## ⚙️ How It Works

1. Launch the application.
2. Select a folder using the **Browse** button.
3. Click **Preview Files** to review the files before organizing them.
4. Check each file's destination category and file size.
5. Review the total file count and combined size.
6. Click **Confirm & Organize** when ready.
7. Watch the live progress bar while files are organized.
8. The application displays the final number of successfully moved and failed files.

The application processes only files directly inside the selected folder and does not recursively organize files inside existing subfolders.

## 🛡️ Safety Features

- Files are not moved until the user confirms the operation.
- The preview window allows users to cancel before any changes are made.
- Existing files are protected from being overwritten through duplicate filename handling.
- Folder selection and file access errors are handled with user-friendly messages.

## 📁 Project Structure

    File-Organizer/
    │
    ├── main.py
    ├── README.md
    ├── LICENSE
    └── .gitignore

## ⚠️ Important Note

Files are moved from their original locations into category folders. Although the application provides a preview and confirmation step, it is recommended to test with a temporary folder before organizing important files.

## 👤 Author

**Hrishikesh Sharma**

GitHub: @RaavanHrishi07

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more information.