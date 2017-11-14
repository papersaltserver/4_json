import unittest
from pprint_json import load_data


class PprintJsonTests(unittest.TestCase):
    def test_data_loded(self):
        json_data = load_data("test_json_data.txt")
        self.assertIsNotNone(json_data)


if __name__ == 'main':
    unittest.main()