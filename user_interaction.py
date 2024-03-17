def confirm_action(question):
    """
    Ask the user to confirm an action with a yes/no question.
    
    Parameters:
    - question: The question to prompt the user with.
    
    Returns:
    True if the user confirms, False otherwise.
    """
    response = input(f"{question} (yes/no): ").strip().lower()
    while response not in ['yes', 'no']:
        print("Please answer with 'yes' or 'no'.")
        response = input(f"{question} (yes/no): ").strip().lower()
    return response == 'yes'

def display_categories_for_deletion(categories):
    """
    Display categories eligible for deletion to the user.
    
    Parameters:
    - categories: A dictionary where keys are category names and values are the number of posts associated with each category.
    """
    print("\nCategories eligible for deletion (less than 3 posts):")
    for category, count in categories.items():
        print(f"- {category}: {count} posts")

def summarize_changes(deleted_categories, errors):
    """
    Provide a summary of the changes made and any errors encountered.
    
    Parameters:
    - deleted_categories: A list of categories that were successfully deleted.
    - errors: A list of error messages encountered during the process.
    """
    if deleted_categories:
        print("\nDeleted Categories:")
        for category in deleted_categories:
            print(f"- {category}")
    else:
        print("\nNo categories were deleted.")

    if errors:
        print("\nErrors encountered:")
        for error in errors:
            print(f"- {error}")
    elif not deleted_categories:
        print("No changes were made.")
    else:
        print("\nAll selected categories were successfully deleted without errors.")
