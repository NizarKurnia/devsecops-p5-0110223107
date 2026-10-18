import unittest
from system_info import get_system_info
from math_operations import hitung_faktorial

class TestAplikasi(unittest.TestCase):
    
    def test_system_info(self):
        info = get_system_info()
        # Memastikan dictionary tidak kosong dan memiliki key "Sistem Operasi"
        self.assertIn("Sistem Operasi", info)
    
    def test_hitung_faktorial(self):
        # Memastikan perhitungan matematika benar
        self.assertEqual(hitung_faktorial(5), 120)
        self.assertEqual(hitung_faktorial(0), 1)

if __name__ == "__main__":
    unittest.main()