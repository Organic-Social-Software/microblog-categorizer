from api_communication import fetch_all_posts, update_post_category
from utils import confirm_action, display_categories_for_deletion
from pprint import pprint  # Add this import at the top of the file

def analyze_categories(app_token):
    """
    Analyze categories from fetched posts and identify which ones should be deleted.
    
    Parameters:
    - app_token: The app token provided by the user for authentication.
    
    Returns:
    A dictionary where keys are category names and values are lists of post IDs associated with each category.
    """
    posts = fetch_all_posts(app_token)  # Adjust the batch size as needed
    print("Sample of fetched posts with metadata:")  # Add this line
    pprint(posts[:20])  # Adjust the number of posts to display as needed
    category_post_map = {}

    for post in posts:
        categories = post.get('properties', {}).get('category', [])
        if categories:  # Check if categories list is not empty
            for category in categories:
                if category not in category_post_map:
                    category_post_map[category] = {post['properties']['uid'][0]}  # Use a set instead of a list
                else:
                    category_post_map[category].add(post['properties']['uid'][0])  # Use add method for a set

    # Debugging print to verify category_post_map contents
    print("Category post map contents:")
    pprint(category_post_map)

    return category_post_map

def delete_categories(app_token):
    """
    Main function to handle the deletion of categories with less than 3 posts.
    
    Parameters:
    - app_token: The app token provided by the user for authentication.
    """
    category_post_map = analyze_categories(app_token)
    # Debugging print to verify category_post_map contents before deletion evaluation
    print("Verifying category_post_map before evaluating for deletion:")
    pprint(category_post_map)
    categories_to_delete = {category: len(posts) for category, posts in category_post_map.items() if len(posts) < 3}

    if not categories_to_delete:
        print("No categories eligible for deletion.")
        return

    display_categories_for_deletion(categories_to_delete)

    if not confirm_action("Proceed with deletion of these categories?"):
        print("Deletion cancelled.")
        return

    deleted_categories = []
    errors = []
    processed_posts = set()  # Track processed posts

    for category, post_ids in category_post_map.items():
        if category in categories_to_delete:
            for post_id in post_ids:
                if post_id in processed_posts:  # Skip if already processed
                    continue
                try:
                    if update_post_category(app_token, post_id, []):  # Removing the category by setting an empty list
                        deleted_categories.append(category)
                        processed_posts.add(post_id)  # Mark as processed
                except Exception as e:
                    errors.append(f"Error updating post {post_id}: {str(e)}")

    summarize_changes(list(set(deleted_categories)), errors)
def summarize_changes(deleted_categories, errors):
    """
    Summarizes the changes made by the deletion process, including any errors encountered.

    Parameters:
    - deleted_categories: A list of categories that were successfully deleted.
    - errors: A list of error messages encountered during the deletion process.
    """
    if deleted_categories:
        print(f"Deleted categories: {', '.join(deleted_categories)}")
    if errors:
        print("Errors encountered:")
        for error in errors:
            print(f"- {error}")
