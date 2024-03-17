def confirm_action(message):
    """
    Prompt the user for confirmation before proceeding with an action.
    
    Parameters:
    - message: The message to display to the user for confirmation.
    
    Returns:
    True if the user confirms, False otherwise.
    """
    response = input(f"{message} (y/n): ").strip().lower()
    return response == 'y'

def display_categories_for_deletion(categories):
    """
    Display categories that are eligible for deletion to the user.
    
    Parameters:
    - categories: A dictionary where keys are category names and values are the number of posts associated with each category.
    """
    print("Categories eligible for deletion (less than 3 posts):")
    for category, count in categories.items():
        print(f"- {category}: {count} posts")

def summarize_changes(deleted_categories, errors):
    """
    Provide a summary of the changes made, including the number of categories deleted and any errors encountered.
    
    Parameters:
    - deleted_categories: A list of categories that were successfully deleted.
    - errors: A list of errors encountered during the deletion process.
    """
    print("\nSummary of Changes:")
    if deleted_categories:
        print("Deleted Categories:")
        for category in deleted_categories:
            print(f"- {category}")
    else:
        print("No categories were deleted.")

    if errors:
        print("\nErrors encountered:")
        for error in errors:
            print(f"- {error}")
    else:
        print("\nNo errors encountered during the process.")