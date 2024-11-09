# Rangefe

## Overview

The Rangefe is a terminal-based application inspired by Ranger File Manager, designed to provide users with a comprehensive and interactive interface for managing files and directories. Built using Python and the `curses` library, this tool allows users to navigate through their file system, preview files, and perform various file operations such as copying, moving, renaming, and deleting. The application supports a wide range of file types, offering previews for documents, spreadsheets, presentations, and more.

## Video Demo:  <URL HERE>

## Features

- **Navigation**: Use arrow keys or `h`, `j`, `k`, `l` for navigating through directories and files.
- **File Operations**: Perform operations like copy, paste, move, rename, and delete files or directories.
- **File Preview**: Preview content of various file types including `.txt`, `.pdf`, `.docx`, `.xlsx`, `.pptx`, and more.
- **Directory Management**: Create new directories and navigate to specific paths.
- **Search Functionality**: Search for files within the current directory.
- **File Information**: View detailed information about files including permissions, type, size, and modification date.
- **Help Screen**: Access a help screen with keyboard shortcuts for easy reference.

## Installation

To run the File Explorer, ensure you have Python installed on your system along with the necessary libraries. You can install the required libraries using pip:

```bash
pip install python-docx PyPDF2 odfpy pandas python-pptx
```

## Usage

Run the application using the following command:

```bash
python file_explorer.py
```

### Keyboard Shortcuts

- **Navigation**:
  - `Arrow Up / k`: Move up in the file list.
  - `Arrow Down / j`: Move down in the file list.
  - `Arrow Left / h`: Go to the parent directory.
  - `Arrow Right / l`: Open the selected directory.

- **File Operations**:
  - `o`: Open the selected file with the default application.
  - `p`: Preview the selected file.
  - `d`: Delete the selected file or directory.
  - `r`: Rename the selected file or directory.
  - `n`: Create a new directory.
  - `c`: Copy the selected file or directory.
  - `v`: Paste the copied file or directory.
  - `m`: Move the selected file or directory to a specified path.

- **Additional Features**:
  - `f`: Find a file or directory by name.
  - `g`: Go to a specific directory path.
  - `i`: Show detailed information about the selected file.
  - `?`: Display the help screen with keyboard shortcuts.
  - `q`: Quit the application.

## File Preview

The File Explorer supports previewing a variety of file types:

- **Text Files**: `.txt`, `.md`, `.csv`, `.py`, etc.
- **Documents**: `.docx`, `.odt`
- **PDFs**: `.pdf`
- **Spreadsheets**: `.xls`, `.xlsx`
- **Presentations**: `.ppt`, `.pptx`

For unsupported file types, a message indicating the lack of preview support is displayed.

## Error Handling

The application includes error handling for various operations. If an error occurs during file operations such as opening, deleting, or moving files, an error message is displayed at the top of the screen.

## Customization

The application uses color pairs for different elements:

- **Directories**: Cyan
- **Files**: White
- **Status Messages**: Yellow
- **Header**: Magenta

These colors can be customized by modifying the `curses.init_pair` function calls in the `main` function.

## Limitations

- The application is designed for Unix-like systems and may require modifications to run on Windows.
- File previews are limited to text extraction and may not fully represent the original formatting of complex documents.

## Conclusion

The File Explorer provides a powerful and flexible interface for managing files directly from the terminal. Its rich feature set and support for various file types make it a valuable tool for users who prefer working in a command-line environment. Whether you're navigating directories, previewing documents, or performing file operations, this application offers a comprehensive solution for your file management needs.
