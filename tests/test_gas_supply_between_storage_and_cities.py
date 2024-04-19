import unittest
import os
from src.gas_supply_between_storage_and_cities import find_and_get_unreachable_cities_supply
cur_path = os.path.dirname(__file__)

class TestGasStorage(unittest.TestCase):
    def test_file_with_value(self):
        find_and_get_unreachable_cities_supply(cur_path + "\\resources\\input_gas_info.txt",cur_path + "\\resources\\output_gas_info.txt")
        with open(
            cur_path + "\\resources\\output_gas_info.txt",
            "r",
            encoding="utf-8",
        ) as file:
            output = file.read()
            expected_output = "('nikopol', ['kyiv', 'lutsk', 'ternopil', 'ivano-frankivsk', 'dnipro'])('dnipro', ['lviv', 'nikopol', 'dashava', 'ternopil', 'chernivtsi', 'kharkiv', 'odesa', 'zaporizhzhia'])"
        self.assertEqual(output, expected_output)

    def test_empty_input_file(self):
        find_and_get_unreachable_cities_supply(
            cur_path + "\\resources\\empty_input_gas_info.txt",
            cur_path + "\\resources\\empty_output_gas_info.txt",
        )
        with open(
            cur_path + "\\resources\\empty_output_gas_info.txt",
            "r",
            encoding="utf-8",
        ) as file:
            output = file.readline().strip()
        expected_output = "-1"
        self.assertEqual(output, expected_output)

    def test_invalid_input_file(self):
        find_and_get_unreachable_cities_supply(
            cur_path + "\\resources\\\invalid_input_gas_info.txt",
            cur_path + "\\resources\\invalid_output_gas_info.txt",
        )
        with open(
            cur_path + "\\resources\\invalid_output_gas_info.txt",
            "r",
            encoding="utf-8",
        ) as file:
            output = file.readline().strip()
        expected_output = "-1"
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()