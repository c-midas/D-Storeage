import unittest
from arweave.client import dstore
from arweave.wallet import Wallet
from arweave.transaction import Transaction

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.client = dstore()
        self.wallet = Wallet("./test_wallet.json")
        self.transaction = Transaction(self.client, self.wallet)

    def test_create_transaction(self):
        transaction = self.transaction.create_transaction("test_data", "text/plain")
        self.assertIn("data", transaction)
