import requests

def fetch_all_posts(headers, batch_size=50):
    """
    Fetches posts in batches from the micro.blog platform.
    Args:
        headers (dict): Headers including the Authorization for API requests.
        batch_size (int): Number of posts to fetch per batch. Defaults to 50.
    Returns:
        list: A list of all posts fetched from the API.
    """
    posts = []
    page = 1
    while True:
        print(f"Fetching posts... Page {page}")  # Loading indication
        url = f"https://micro.blog/micropub?q=source&page={page}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to fetch posts. Status code: {response.status_code}")
            break
        data = response.json()
        if not data['items']:
            break
        posts.extend(data['items'])
        page += 1
        if len(posts) >= 1835:  # Adjust based on total posts
            break
    return posts

def update_post_category(post_id, new_categories, headers):
    """
    Updates the category of a post by making a PATCH request to the Micropub API.
    Args:
        post_id (str): The ID of the post to update.
        new_categories (list): A list of categories to be associated with the post.
        headers (dict): Headers including the Authorization for API requests.
    Returns:
        bool: True if the update was successful, False otherwise.
    """
    url = "https://micro.blog/micropub"
    data = {
        "action": "update",
        "url": f"https://micro.blog/posts/{post_id}",  # This might need adjustment based on Micropub's requirements
        "replace": {"category": new_categories}
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return True
    else:
        print(f"Failed to update post {post_id}. Status code: {response.status_code}")
        return False

def remove_category_from_posts(posts, category_to_remove, headers):
    """
    Iterates through a list of posts, removing a specified category from each post's metadata.
    Args:
        posts (list): A list of posts to update.
        category_to_remove (str): The category to remove from each post.
        headers (dict): Headers including the Authorization for API requests.
    Returns:
        int: The number of posts successfully updated.
    """
    updated_count = 0
    for post in posts:
        if category_to_remove in post.get('category', []):
            new_categories = [cat for cat in post.get('category', []) if cat != category_to_remove]
            if update_post_category(post['id'], new_categories, headers):
                updated_count += 1
    return updated_count
