# File Organizer 📁

A simple and user-friendly Python desktop application that automatically organizes files into categorized folders based on their file extensions.

## ✨ Features

- Select any folder using the Browse button
- Automatically organize files into categories
- Supports images, documents, videos, audio, archives and code files
- Moves unsupported file types into an Others folder
- Prevents duplicate filename conflicts
- Confirmation before organizing files
- Displays a summary of successfully moved and failed files
- Simple graphical user interface built with Tkinter

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
2. Select a folder using the Browse button.
3. Click Organize Files.
4. Confirm the operation.
5. Files are moved into folders based on their extensions.

The application processes files directly inside the selected folder and does not recursively organize subfolders.

## 📁 Project Structure

    File-Organizer/
    │
    ├── main.py
    ├── README.md
    └── .gitignore

## ⚠️ Important Note

Files are moved from their original locations into category folders. Always test with a temporary folder before organizing important files.

## 👤 Author

**Hrishikesh Sharma**

GitHub: [@RaavanHrishi07](https://github.com/RaavanHrishi07)

## 📄 License

This project is licensed under the MIT License.