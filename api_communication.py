import requests
from auth import authenticate_request

class APIError(Exception):
    """Custom exception for API errors."""
    pass

class NetworkError(APIError):
    """Exception for network-related errors."""
    pass

class AuthenticationError(APIError):
    """Exception for authentication errors."""
    pass

class UserNotFoundError(APIError):
    """Exception for user not found errors."""
    pass

def fetch_all_posts(app_token):
    """
    Fetch all posts from the micro.blog account using pagination.
    
    Parameters:
    - app_token: The app token provided by the user for authentication.
    
    Returns:
    A list of all posts fetched from the micro.blog account.
    """
    all_posts = []
    page = 1
    print("Fetching posts...", end="")
    
    while True:
        url = f"https://micro.blog/micropub?q=source&page={page}"
        headers = authenticate_request(app_token)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if not data["items"]:  # Check if "items" list is empty
                print("\rFetching posts... Done.")
                break  # No more posts to fetch
            all_posts.extend(data["items"])
            print(f"\rFetched {len(all_posts)} posts...", end="")
            page += 1
            if len(all_posts) > 100:  # Assuming 100 is a reasonable upper limit for your use case
                print("\rFetched posts limit reached. Aborting...")
                break
        else:
            print("\rFailed to fetch posts. Please check your network connection and try again.")
            break
    return all_posts

def update_post_category(app_token, post_id, categories):
    """
    Update the category of a specific post.
    
    Parameters:
    - app_token: The app token provided by the user for authentication.
    - post_id: The ID of the post to update.
    - categories: A list of categories to be associated with the post.
    
    Returns:
    True if the update was successful, False otherwise.
    """
    url = f"https://micro.blog/micropub/posts/{post_id}"
    headers = authenticate_request(app_token)
    data = {
        "action": "update",
        "url": f"https://micro.blog/posts/{post_id}",
        "replace": {"category": categories}
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to update post {post_id} with categories {categories}.")
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.content}")
        raise APIError("Failed to update post category. Please check your network connection and try again.")
    
    return True
