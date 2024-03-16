import auth
import api_communication
import data_processing
import user_interaction

def main():
    # Step 1: Authentication
    app_token = auth.get_app_token()
    headers = auth.authenticate_with_token(app_token)
    if not auth.test_authentication(headers):
        return

    # Step 2: Fetching Posts and Categories
    print("Fetching all posts from micro.blog...")
    posts = api_communication.fetch_all_posts(headers)
    if not posts:
        print("No posts found. Exiting...")
        return

    # Debugging: Print the first few posts to review their structure and categories
    print("Sample posts for review:", posts[:5])

    # Step 3: Aggregating Category Information
    category_counts = data_processing.aggregate_categories(posts)
    categories_to_delete = data_processing.identify_categories_to_delete(category_counts)

    # Step 4: Confirming Categories to Delete
    if not user_interaction.confirm_deletion(categories_to_delete):
        print("Category deletion cancelled.")
        return

    # Step 5: Deleting Categories
    deleted_categories = []
    errors = []
    for category in categories_to_delete:
        filtered_posts = data_processing.filter_posts_by_category(posts, category)
        success = True
        for post in filtered_posts:
            post_id = post['id']
            new_categories = [cat for cat in post.get('category', []) if cat != category]
            if not api_communication.update_post_category(post_id, new_categories, headers):
                success = False
                errors.append(f"Failed to update category for post {post_id}")
                break
        if success:
            deleted_categories.append(category)

    # Step 6: Final Confirmation
    user_interaction.display_final_confirmation(deleted_categories, errors)

if __name__ == "__main__":
    main()
