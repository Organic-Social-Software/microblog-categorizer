def aggregate_categories(posts):
    """
    Aggregates categories from a list of posts, counting the number of posts in each category.
    Args:
        posts (list): A list of posts fetched from the API.
    Returns:
        dict: A dictionary with categories as keys and the number of posts in each category as values.
    """
    category_counts = {}
    for post in posts:
        categories = post.get('category', [])
        for category in categories:
            if category in category_counts:
                category_counts[category] += 1
            else:
                category_counts[category] = 1
    return category_counts

def identify_categories_to_delete(category_counts):
    """
    Identifies categories with fewer than 3 posts.
    Args:
        category_counts (dict): A dictionary with categories as keys and the number of posts in each category as values.
    Returns:
        list: A list of categories that have fewer than 3 posts.
    """
    categories_to_delete = [category for category, count in category_counts.items() if count < 3]
    print(categories_to_delete)  # Add this line to print categories identified for deletion
    return categories_to_delete

def filter_posts_by_category(posts, category):
    """
    Filters posts by a specific category.
    Args:
        posts (list): A list of posts fetched from the API.
        category (str): The category to filter posts by.
    Returns:
        list: A list of posts that are tagged with the specified category.
    """
    filtered_posts = [post for post in posts if category in post.get('category', [])]
    return filtered_posts

def present_categories_for_review(categories_to_delete, category_counts):
    """
    Presents a list of categories marked for deletion, along with the number of posts they contain, for user review.
    Args:
        categories_to_delete (list): A list of categories identified for deletion.
        category_counts (dict): A dictionary with categories as keys and the number of posts in each category as values.
    Returns:
        None
    """
    print("Categories marked for deletion (with fewer than 3 posts):")
    for category in categories_to_delete:
        print(f"- {category}: {category_counts[category]} posts")
