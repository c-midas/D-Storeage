# Arweave Client Library

A lightweight Python library for interacting with the Arweave blockchain's HTTP API. This library simplifies making `GET` and `POST` requests to the Arweave network, allowing developers to focus on higher-level blockchain functionality.

## Features

- **Configurable API URL:** Default to `https://arweave.net`, with the flexibility to use custom URLs.
- **HTTP Abstraction:** Provides methods for `GET` and `POST` requests to interact with Arweave endpoints.
- **Error Handling:** Automatically handles HTTP errors with meaningful exceptions.

## Installation

To install the package, clone the repository and install it locally using `pip`:

```bash
git clone https://github.com/c-midas/D-Storeage.git
cd D-Storeage
pip install .
```
## Usage
### Importing the Library

```python
from arweave_client import ArweaveClient
```
### Initializing the Client

```python
client = ArweaveClient(api_url="https://arweave.net")  # Default URL
```
### Sending a POST Request

```python
transaction_data = {"data": "example_data"}
try:
    response = client.post("tx", transaction_data)
    print("POST Response:", response)
except requests.exceptions.HTTPError as e:
    print(f"Error during POST request: {e}")
```
### Sending a GET Request
```python
transaction_id = "example_transaction_id"
try:
    response = client.get(f"tx/{transaction_id}")
    print("GET Response:", response)
except requests.exceptions.HTTPError as e:
    print(f"Error during GET request: {e}")
```
## Examples
### Posting a Transaction

```python
from arweave_client import ArweaveClient

# Initialize the client
client = ArweaveClient()

# Create transaction data
transaction_data = {
    "data": "example_data_in_hexadecimal_format",
    "tags": [{"name": "Content-Type", "value": "text/plain"}]
}

# Post the transaction
try:
    response = client.post("tx", transaction_data)
    print(f"Transaction created successfully: {response}")
except requests.exceptions.HTTPError as e:
    print(f"Error creating transaction: {e}")
```
### Fetching Transaction Details

```python
from arweave_client import ArweaveClient

# Initialize the client
client = ArweaveClient()

# Transaction ID to fetch
transaction_id = "example_transaction_id"

# Get transaction details
try:
    response = client.get(f"tx/{transaction_id}")
    print(f"Transaction details: {response}")
except requests.exceptions.HTTPError as e:
    print(f"Error fetching transaction: {e}")
```
## Error Handling
The library uses requests' `built-in raise_for_status()` for error handling. Any failed HTTP request will raise a `requests.exceptions.HTTPError` with detailed information about the error.

## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (feature/your-feature-name).
3. Commit your changes.
4. Push to your fork.
5. Create a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.