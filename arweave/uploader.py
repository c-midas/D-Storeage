import mimetypes

class FileUploader:
    """
    A utility class for uploading files to a decentralized network via a transaction handler.

    The `FileUploader` class reads files, determines their MIME types, and uploads them 
    using a provided transaction handler. The lifecycle includes creating, signing, and 
    submitting a transaction to the network.

    Attributes:
        transaction_handler: An instance of a transaction handler responsible for creating,
                             signing, and submitting transactions.
    """

    def __init__(self, transaction_handler):
        """
        Initializes the FileUploader with a transaction handler.

        Args:
            transaction_handler: An object responsible for handling transaction operations.
                                 Must implement methods for creating, signing, and submitting
                                 transactions.
        """
        self.transaction_handler = transaction_handler

    def upload_file(self, file_path: str):
        """
        Uploads a file to the network using the transaction handler.

        This method reads the file from the specified path, encodes its content as hexadecimal,
        and assigns an appropriate MIME type. It then creates, signs, and submits a transaction
        for the file's data.

        Args:
            file_path (str): The absolute or relative path of the file to be uploaded.

        Returns:
            str: The transaction ID of the successfully submitted transaction.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            IOError: If there is an error reading the file.
        """
        # Open the file in binary mode and read its content
        with open(file_path, "rb") as file:
            data = file.read()

        # Guess the MIME type of the file, default to "application/octet-stream" if unknown
        content_type = mimetypes.guess_type(file_path)[0] or "application/octet-stream"

        # Create a transaction for the file data
        transaction = self.transaction_handler.create_transaction(data.hex(), content_type)

        # Sign the created transaction
        signed_transaction = self.transaction_handler.sign_transaction(transaction)

        # Submit the signed transaction to the network and return the transaction ID
        return self.transaction_handler.submit_transaction(signed_transaction)
