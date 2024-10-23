import requests
import os

def blacklist(api_key):
    url = "https://api.abuseipdb.com/api/v2/blacklist"
    params = {
        'confidenceMinimum': 90
    }
    headers = {
        'Key': api_key,
        'Accept': 'application/json'
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raises an error for bad responses (4xx or 5xx)
        return response.json()  # Return the JSON response if successful
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Print the HTTP error
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")  # Print any other errors
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Handle any other exceptions

# Example usage
result = blacklist(os.getenv('API_ABUSE'))
print(result)