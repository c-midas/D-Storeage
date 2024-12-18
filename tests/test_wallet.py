import unittest
import json
import os
from arweave.wallet import Wallet


class TestWallet(unittest.TestCase):
    def setUp(self):
        """
        Setup a mock wallet file for testing.
        """
        self.mock_wallet_path = "test_wallet.json"
        self.mock_wallet_data = {
            "kty": "RSA",
            "n": "mock_public_key",
            "e": "AQAB",
            "d": "mock_private_key",
            "p": "mock_prime1",
            "q": "mock_prime2",
        }

        # Create a mock wallet file
        with open(self.mock_wallet_path, "w") as file:
            json.dump(self.mock_wallet_data, file)

    def tearDown(self):
        """
        Clean up the mock wallet file after tests.
        """
        if os.path.exists(self.mock_wallet_path):
            os.remove(self.mock_wallet_path)

    def test_load_wallet_success(self):
        """
        Test that the wallet file loads correctly when valid.
        """
        wallet = Wallet(self.mock_wallet_path)
        self.assertEqual(wallet.wallet, self.mock_wallet_data)

    def test_load_wallet_file_not_found(self):
        """
        Test that the appropriate error is raised when the wallet file is missing.
        """
        with self.assertRaises(FileNotFoundError):
            Wallet("nonexistent_wallet.json")

    def test_load_wallet_invalid_format(self):
        """
        Test that the appropriate error is raised for invalid wallet file format.
        """
        # Create an invalid wallet file
        invalid_wallet_path = "invalid_wallet.json"
        with open(invalid_wallet_path, "w") as file:
            file.write("not_a_valid_json")

        with self.assertRaises(ValueError):
            Wallet(invalid_wallet_path)

        # Clean up
        os.remove(invalid_wallet_path)

    def test_wallet_file_content(self):
        """
        Test that the wallet content matches the expected data structure.
        """
        wallet = Wallet(self.mock_wallet_path)
        self.assertIn("kty", wallet.wallet)
        self.assertIn("n", wallet.wallet)
        self.assertIn("d", wallet.wallet)
        self.assertEqual(wallet.wallet["kty"], "RSA")
        self.assertEqual(wallet.wallet["n"], "mock_public_key")


if __name__ == "__main__":
    unittest.main()
