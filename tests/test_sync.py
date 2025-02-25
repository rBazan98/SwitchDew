import unittest
from sync import LocalSync

class TestLocalSync(unittest.TestCase):
    def setUp(self):
        self.local_sync = LocalSync("./test_folder")

    def test_file_exists(self):
        self.assertFalse(self.local_sync.file_exists("no_exist.txt"))

if __name__ == "__main__":
    unittest.main()