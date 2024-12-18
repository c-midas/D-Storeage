import json

class Wallet:
    """
    A class to manage the loading and handling of wallet files for blockchain transactions.

    The `Wallet` class reads wallet files in JSON format, validates their structure, 
    and stores the loaded wallet data for use in signing and managing blockchain transactions.

    Attributes:
        wallet_path (str): The file path to the wallet JSON file.
        wallet (dict): The loaded wallet data containing keys and other required information.
    """

    def __init__(self, wallet_path: str):
        """
        Initializes the Wallet class with the path to a wallet file.

        Args:
            wallet_path (str): The file path to the wallet JSON file.

        Raises:
            FileNotFoundError: If the specified wallet file does not exist.
            ValueError: If the wallet file is invalid or not in JSON format.
        """
        self.wallet_path = wallet_path
        self.wallet = self.load_wallet()

    def load_wallet(self):
        """
        Loads the wallet data from the specified JSON file.

        This method reads the wallet file, parses its content, and validates its format. 
        It raises appropriate exceptions for missing files or invalid formats.

        Returns:
            dict: A dictionary containing the wallet data (e.g., private keys, public keys).

        Raises:
            FileNotFoundError: If the wallet file cannot be found at the specified path.
            ValueError: If the wallet file is not in a valid JSON format.
        """
        try:
            # Open the wallet file and load its content as a dictionary
            with open(self.wallet_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("Wallet file not found. Please check the file path.")
        except json.JSONDecodeError:
            raise ValueError("Invalid wallet file format. Ensure the file contains valid JSON.")
