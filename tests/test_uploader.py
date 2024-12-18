from arweave.client import ArweaveClient
from arweave.wallet import Wallet
from arweave.transaction import Transaction
from arweave.uploader import FileUploader

client = ArweaveClient()
wallet = Wallet("./wallet.json")
transaction_handler = Transaction(client, wallet)
uploader = FileUploader(transaction_handler)

file_path = "example.txt"
transaction_id = uploader.upload_file(file_path)
print(f"File uploaded successfully with transaction ID: {transaction_id}")
