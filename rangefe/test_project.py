import os
import sys
import unittest
from unittest.mock import patch, mock_open, MagicMock
import shutil
import zipfile
import tarfile

# Add the directory containing project.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from project import FileExplorer  # Import the FileExplorer class from project.py

class TestFileExplorer(unittest.TestCase):
    
    def setUp(self):
        # Mock the curses module functions
        self.curses_patcher = patch('curses.initscr', return_value=MagicMock())
        self.curses_patcher.start()

        # Mock other curses functions used in FileExplorer
        self.mock_curses = patch('curses.color_pair', return_value=1)
        self.mock_curses.start()
        self.mock_curses_newwin = patch('curses.newwin', return_value=MagicMock())
        self.mock_curses_newwin.start()

        self.mock_stdscr = MagicMock()
        self.explorer = FileExplorer(self.mock_stdscr)
        self.explorer.current_path = os.getcwd()  # Set a known path for testing

    def tearDown(self):
        # Stop the patchers for curses
        self.curses_patcher.stop()
        self.mock_curses.stop()
        self.mock_curses_newwin.stop()

    def test_human_readable_size(self):
        self.assertEqual(self.explorer.human_readable_size(1023), "1023.00 B")
        self.assertEqual(self.explorer.human_readable_size(1024), "1.00 KB")
        self.assertEqual(self.explorer.human_readable_size(1048576), "1.00 MB")

    def test_get_file_info(self):
        with patch('os.stat') as mock_stat:
            mock_stat.return_value.st_size = 1024
            mock_stat.return_value.st_mtime = 1609459200  # 2021-01-01 00:00:00
            mock_stat.return_value.st_mode = 33279  # rwxrwxrwx permissions
            info = self.explorer.get_file_info('test.txt')
            self.assertEqual(info, ('-rwxrwxrwx', '.txt', '1.00 KB', '2021-01-01 00:00:00'))

    @patch('os.listdir', return_value=['file1.txt', 'file2.doc', 'dir1'])
    def test_load_files(self, mock_listdir):
        self.explorer.load_files()
        self.assertEqual(self.explorer.file_list, ['dir1', 'file1.txt', 'file2.doc'])

    @patch('os.path.isdir', return_value=True)
    @patch('os.listdir', return_value=['subfile1.txt', 'subfile2.doc'])
    def test_load_directory_contents(self, mock_listdir, mock_isdir):
        self.explorer.load_directory_contents('dir1')
        self.assertEqual(self.explorer.selected_directory_contents, ['subfile1.txt', 'subfile2.doc'])

    @patch('os.rename')
    def test_rename_file(self, mock_rename):
        with patch('project.FileExplorer.prompt_input', return_value='new_name.txt'):
            self.explorer.file_list = ['old_name.txt']
            self.explorer.current_selection = 0
            self.explorer.rename_file()
            mock_rename.assert_called_once_with(os.path.join(self.explorer.current_path, 'old_name.txt'),
                                                os.path.join(self.explorer.current_path, 'new_name.txt'))

    @patch('os.mkdir')
    def test_create_directory(self, mock_mkdir):
        with patch('project.FileExplorer.prompt_input', return_value='new_directory'):
            self.explorer.create_directory()
            mock_mkdir.assert_called_once_with(os.path.join(self.explorer.current_path, 'new_directory'))

    @patch('shutil.rmtree')
    @patch('os.remove')
    def test_delete_file(self, mock_remove, mock_rmtree):
        self.explorer.file_list = ['file_to_delete.txt']
        self.explorer.current_selection = 0
        # Create a dummy file to delete
        with open(os.path.join(self.explorer.current_path, 'file_to_delete.txt'), 'w') as f:
            f.write('dummy content')

        with patch('project.FileExplorer.prompt_confirmation', return_value='y'):
            self.explorer.delete_file()
            mock_remove.assert_called_once_with(os.path.join(self.explorer.current_path, 'file_to_delete.txt'))

    def test_delete_file_no_confirmation(self):
        # Create a dummy file to test deletion
        with open(os.path.join(self.explorer.current_path, 'file_to_delete.txt'), 'w') as f:
            f.write('dummy content')

        self.explorer.file_list = ['file_to_delete.txt']
        self.explorer.current_selection = 0
        with patch('project.FileExplorer.prompt_confirmation', return_value='n'):
            self.explorer.delete_file()
            self.assertTrue(os.path.exists(os.path.join(self.explorer.current_path, 'file_to_delete.txt')))

    @patch('shutil.copy2')
    def test_copy_file(self, mock_copy2):
        self.explorer.file_list = ['file_to_copy.txt']
        self.explorer.current_selection = 0
        self.explorer.copy_file()
        self.assertEqual(self.explorer.copied_file_path, os.path.join(self.explorer.current_path, 'file_to_copy.txt'))

    @patch('shutil.copy2')
    def test_paste_file(self, mock_copy2):
        self.explorer.copied_file_path = os.path.join(self.explorer.current_path, 'file_to_copy.txt')
        self.explorer.paste_file()
        mock_copy2.assert_called_once_with(self.explorer.copied_file_path,
                                           os.path.join(self.explorer.current_path, 'file_to_copy.txt'))

    @patch('zipfile.ZipFile')
    def test_compress_files(self, mock_zipfile):
        with patch('project.FileExplorer.prompt_input', return_value='compressed'):
            self.explorer.file_list = ['file_to_compress.txt']
            self.explorer.current_selection = 0
            self.explorer.compress_files()
            mock_zipfile.assert_called_once()

    @patch('zipfile.ZipFile')
    def test_decompress_file_zip(self, mock_zipfile):
        self.explorer.file_list = ['file_to_decompress.zip']
        self.explorer.current_selection = 0
        self.explorer.decompress_file()
        mock_zipfile.assert_called_once()

    @patch('tarfile.open')
    def test_decompress_file_tar(self, mock_tarfile):
        self.explorer.file_list = ['file_to_decompress.tar.gz']
        self.explorer.current_selection = 0
        self.explorer.decompress_file()
        mock_tarfile.assert_called_once()

    @patch('os.path.isdir', return_value=True)
    @patch('os.path.exists', return_value=True)
    def test_go_to_directory(self, mock_exists, mock_isdir):
        with patch('project.FileExplorer.prompt_input', return_value='/some/path'):
            self.explorer.go_to_directory()
            self.assertEqual(self.explorer.current_path, '/some/path')

    @patch('project.FileExplorer.prompt_input', return_value='file')
    @patch('os.listdir', return_value=['file1.txt', 'file2.doc', 'file3.txt'])
    def test_find(self, mock_listdir, mock_input):
        self.explorer.load_files()
        self.explorer.find()
        self.assertIn('file1.txt', self.explorer.file_list)
        self.assertIn('file3.txt', self.explorer.file_list)

if __name__ == '__main__':
    unittest.main()