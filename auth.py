import os
import requests

def get_app_token():
    """
    Prompts the user to enter their micro.blog app token. Advises on secure storage practices.
    Returns:
        app_token (str): The app token provided by the user.
    """
    print("Please enter your micro.blog app token.")
    print("For security reasons, it's recommended to store your token in an environment variable or a secure vault.")
    app_token = input("App Token: ")
    return app_token

def authenticate_with_token(app_token):
    """
    Prepares the authorization header for API requests using the provided app token.
    Args:
        app_token (str): The app token for micro.blog API authentication.
    Returns:
        headers (dict): Headers including the Authorization field for API requests.
    """
    headers = {
        'Authorization': f'Bearer {app_token}',
        'Content-Type': 'application/json'
    }
    return headers

def test_authentication(headers):
    """
    Tests the provided authentication headers by making a simple API call.
    Args:
        headers (dict): Headers including the Authorization for API requests.
    Returns:
        bool: True if authentication is successful, False otherwise.
    """
    test_url = "https://micro.blog/micropub"
    response = requests.get(test_url, headers=headers)
    if response.status_code == 200:
        print("Authentication successful.")
        return True
    else:
        print("Authentication failed. Please check your app token and try again.")
        return False
