# File Explorer

A terminal-based file explorer inspired mainly by Range File Manager, built using Python and the `curses` library. This application allows users to navigate through directories, preview files, manage files (copy, move, delete, rename), and compress or decompress files. It provides a user-friendly interface for file management directly from the terminal, making it a powerful tool for users who prefer command-line operations.

## Video Demo:  <URL HERE>

## Features

- **Directory Navigation**: Easily navigate through directories using the keyboard. The application supports moving up to parent directories and entering subdirectories.
- **File Management**: Perform various file operations such as creating, renaming, copying, moving, and deleting files and directories.
- **File Preview**: Preview the contents of text-based files, including `.txt`, `.docx`, `.pdf`, and more, directly within the application.
- **Search Functionality**: Quickly search for files by name, allowing for efficient file management in directories with many files.
- **Compression and Decompression**: Compress files and directories into ZIP format and decompress ZIP and tar.gz files, making it easier to manage storage.
- **Detailed File Information**: View detailed information about files, including permissions, size, type, and last modified date.

## Requirements

To run this application, you need:

- **Python 3.x**: Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **Required Python packages**: The application uses several external libraries. You can install the required packages using pip:

```bash
pip install python-docx pypdf odfpy pandas python-pptx
```

These libraries enable the application to handle various file types and operations efficiently.

## Installation

1. **Clone the Repository**: Start by cloning the repository to your local machine. Open your terminal and run:

```bash
git clone https://github.com/rtmali/cs50p_project.git
```

2. **Navigate to the Project Directory**: Change into the project directory:

```bash
cd cs50p_project/rangefe
```

3. **Install Required Packages**: Use pip to install the necessary Python packages as mentioned above.

## Usage

To run the file explorer, execute the following command in your terminal:

```bash
python project.py
```

Upon launching the application, you will be greeted with a user-friendly interface that displays the current directory's contents. You can navigate through files and directories using the keyboard shortcuts outlined below.

### Keyboard Shortcuts

The application is designed to be intuitive, with several keyboard shortcuts to enhance usability:

- **Arrow Up / Arrow Down**: Navigate through files and directories.
- **Arrow Left**: Go to the parent directory.
- **Arrow Right**: Open the selected directory.
- **o**: Open the selected file with the default application associated with that file type.
- **p**: Preview the contents of the selected file.
- **d**: Delete the selected file or directory after confirmation.
- **r**: Rename the selected file or directory.
- **m**: Move the selected file or directory to a new location.
- **n**: Create a new directory in the current location.
- **f**: Find a file or directory by name.
- **g**: Go to a specific directory by entering its path.
- **i**: Show detailed information about the selected file.
- **?**: Display a help screen with keyboard shortcuts.
- **z**: Compress the selected file or directory into a ZIP file.
- **e**: Decompress the selected ZIP or tar.gz file.
- **q**: Quit the application.

## Contributing

Contributions to this project are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to submit a pull request. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear messages.
4. Push your changes to your forked repository.
5. Open a pull request to the main repository.

## License

This project is licensed under the MIT License. You can view the full license text in the [LICENSE](LICENSE) file included in the repository. This allows you to use, modify, and distribute the software freely, provided that the original license is maintained.

## Acknowledgments

- Special thanks to the developers of the libraries used in this project, including `python-docx`, `PyPDF2`, `odfpy`, `pandas`, and `python-pptx`, which enable the application to handle various file formats and operations.
- Inspired by various terminal-based file managers, this project aims to provide a simple yet powerful tool for file management in a command-line environment.

## Future Enhancements

While the current version of the File Explorer provides a robust set of features, there are always opportunities for improvement. Future enhancements may include:

- Support for additional file formats for previewing.
- Improved error handling and user feedback.
- A more advanced search functionality that supports regular expressions.
- Integration with cloud storage services for remote file management.

## Conclusion

The File Explorer is a powerful tool for users who prefer working in a terminal environment. With its comprehensive set of features, it simplifies file management tasks and enhances productivity. Whether you are a developer, system administrator, or casual user, this application can help you navigate and manage your files more efficiently.

Feel free to explore the code, contribute, and make this project even better!
