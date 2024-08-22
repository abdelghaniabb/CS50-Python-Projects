#!/usr/bin/python3

import unittest
from project import read_file, extract_names, calculate, check_contributed, total

class TestProject(unittest.TestCase):

    def setUp(self):
        """Set up mock data for testing"""
        self.mock_data = [
            ["adam;rafik;rida;karim"],
            ["300;350 - rida;400 - adam;390"],
            ["250 - adam;200;320;280 - rida"],
            ["310;290 - karim;350;400 - adam"],
            ["270 - rafik;310;400;360 - rida"],
            ["290;330 - karim;370 - adam;390"],
            ["320;280 - rida;340;310 - karim"],
            ["300;250 - adam;330 - rafik;360"]
        ]

    def test_read_file(self):
        """Test read_file function"""
        # Write mock data to 'data.csv'
        with open('data.csv', 'w', encoding='utf-8') as outfile:
            for row in self.mock_data:
                outfile.write(';'.join(row) + '\n')

        # Expected output is same as mock data
        expected_output = [
            ["adam;rafik;rida;karim"],
            ["300;350 - rida;400 - adam;390"],
            ["250 - adam;200;320;280 - rida"],
            ["310;290 - karim;350;400 - adam"],
            ["270 - rafik;310;400;360 - rida"],
            ["290;330 - karim;370 - adam;390"],
            ["320;280 - rida;340;310 - karim"],
            ["300;250 - adam;330 - rafik;360"]
        ]

        self.assertEqual(read_file(), expected_output)

    def test_extract_names(self):
        """Test extract_names function"""
        names, data = extract_names(self.mock_data)
        expected_names = ["adam", "rafik", "rida", "karim"]
        expected_data = [
            ["300", "350 - rida", "400 - adam", "390"],
            ["250 - adam", "200", "320", "280 - rida"],
            ["310", "290 - karim", "350", "400 - adam"],
            ["270 - rafik", "310", "400", "360 - rida"],
            ["290", "330 - karim", "370 - adam", "390"],
            ["320", "280 - rida", "340", "310 - karim"],
            ["300", "250 - adam", "330 - rafik", "360"]
        ]
        self.assertEqual(names, expected_names)
        self.assertEqual(data, expected_data)

    def test_calculate(self):
        """Test calculate function"""
        names, data = extract_names(self.mock_data)
        calculate(names, data)
        expected_totals = {
            'adam': -38.33333333333334,
            'rafik': -424.9999999999999,
            'rida': 298.33333333333337,
            'karim': 165.00000000000006
        }
        self.assertEqual(total, expected_totals)
        
    def test_check_contributed(self):
        """Test check_contributed function"""
        names = ["adam", "rafik", "rida", "karim"]
        total.clear()
        for name in names:
            total[name] = 0

        check_contributed(names, "adam", "250 - adam")
        expected_totals = {
            'adam': 250.0,
            'rafik': -83.33333333333333,
            'rida': -83.33333333333333,
            'karim': -83.33333333333333
        }
        self.assertEqual(total, expected_totals)

if __name__ == '__main__':
    unittest.main()
