import unittest
import sys
import os

script_dir = os.path.dirname(os.path.relpath(__file__))
sys.path.append(os.path.dirname(script_dir))
from src.gas_supply_between_storage_and_cities import (
    find_and_get_unreachable_cities_supply,
)


class TestGasStorage(unittest.TestCase):
    def test_file_with_value(self):
        file_input = "resources/input_gas_info.txt"
        file_output = "resources/output_gas_info.txt"

        find_and_get_unreachable_cities_supply(file_input, file_output)

        with open(file_output, "r", encoding="utf-8") as file:
            output = file.read()
            expected_output = "('nikopol', ['kyiv', 'lutsk', 'ternopil', 'ivano-frankivsk', 'dnipro'])('dnipro', ['lviv', 'nikopol', 'dashava', 'ternopil', 'chernivtsi', 'kharkiv', 'odesa', 'zaporizhzhia'])"
        self.assertEqual(output, expected_output)

    def test_empty_input_file(self):
        file_input = "resources/empty_input_gas_info.txt"
        file_output = "resources/empty_output_gas_info.txt"

        find_and_get_unreachable_cities_supply(file_input, file_output)
        with open(file_output, "r", encoding="utf-8") as file:
            output = file.readline().strip()
        expected_output = "-1"
        self.assertEqual(output, expected_output)

    def test_invalid_input_file(self):
        file_input = "resources/invalid_input_gas_info.txt"
        file_output = "resources/invalid_output_gas_info.txt"

        find_and_get_unreachable_cities_supply(file_input, file_output)
        with open(file_output, "r", encoding="utf-8") as file:
            output = file.readline().strip()
        expected_output = "-1"
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
