import requests

class AuthenticationError(Exception):
    """Custom exception for authentication errors."""
    pass

def get_app_token():
    """
    Prompt the user for the app token and return it.
    This function ensures the app token is entered before proceeding.
    """
    app_token = input("Please enter your micro.blog app token: ").strip()
    if not app_token:
        raise ValueError("App token cannot be empty.")
    return app_token

def authenticate_request(app_token):
    """
    Prepare the authentication header for API requests using the provided app token.
    
    Parameters:
    - app_token: The app token provided by the user for authentication.
    
    Returns:
    A dictionary containing the Authorization header.
    """
    if not app_token:
        raise AuthenticationError("App token is required for authentication.")
    
    headers = {
        "Authorization": f"Bearer {app_token}"
    }
    return headers

def test_authentication(app_token):
    """
    Test the provided app token by making a simple authenticated request to the micro.blog API.
    
    Parameters:
    - app_token: The app token provided by the user.
    
    Raises:
    - AuthenticationError: If the authentication fails.
    """
    headers = authenticate_request(app_token)
    response = requests.get("https://micro.blog/micropub", headers=headers)
    
    if response.status_code != 200:
        raise AuthenticationError("Failed to authenticate with the provided app token. Please check your token and try again.")

if __name__ == "__main__":
    try:
        app_token = get_app_token()
        test_authentication(app_token)
        print("Authentication successful.")
    except (ValueError, AuthenticationError) as e:
        print(f"Error: {e}")
