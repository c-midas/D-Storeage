import requests

class ArweaveClient:
    """
    A lightweight client for interacting with the Arweave blockchain's HTTP API.

    The `ArweaveClient` simplifies sending HTTP requests to the Arweave network. 
    It provides methods to perform `GET` and `POST` operations, abstracting low-level
    HTTP logic while ensuring proper error handling and response parsing.

    Attributes:
        api_url (str): The base URL of the Arweave API. Defaults to "https://arweave.net".
    """

    def __init__(self, api_url="https://arweave.net"):
        """
        Initializes the ArweaveClient with a specified API base URL.

        Args:
            api_url (str): The base URL for the Arweave network API. Defaults to "https://arweave.net".
        """
        self.api_url = api_url

    def post(self, endpoint: str, data: dict):
        """
        Sends an HTTP POST request to the specified endpoint.

        This method constructs the full API URL by appending the given endpoint to the base URL.
        It sends a JSON payload as part of the POST request and returns the parsed JSON response.

        Args:
            endpoint (str): The API endpoint to send the request to (e.g., "tx").
            data (dict): The JSON data to include in the POST request body.

        Returns:
            dict: The JSON response from the server.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request fails or returns an error status code.
        """
        # Construct the full URL and send the POST request
        response = requests.post(f"{self.api_url}/{endpoint}", json=data)

        # Raise an HTTPError for unsuccessful responses
        response.raise_for_status()

        # Parse and return the JSON response
        return response.json()

    def get(self, endpoint: str, params: dict = None):
        """
        Sends an HTTP GET request to the specified endpoint.

        This method constructs the full API URL by appending the given endpoint to the base URL.
        Optionally, query parameters can be included in the request.

        Args:
            endpoint (str): The API endpoint to send the request to (e.g., "tx/<transaction_id>").
            params (dict, optional): A dictionary of query parameters to include in the request. Defaults to None.

        Returns:
            dict: The JSON response from the server.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request fails or returns an error status code.
        """
        # Construct the full URL and send the GET request
        response = requests.get(f"{self.api_url}/{endpoint}", params=params)

        # Raise an HTTPError for unsuccessful responses
        response.raise_for_status()

        # Parse and return the JSON response
        return response.json()
