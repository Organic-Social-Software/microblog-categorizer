def confirm_deletion(categories_to_delete):
    """
    Prompts the user for confirmation before proceeding with the deletion of categories.
    Args:
        categories_to_delete (list): A list of categories identified for deletion.
    Returns:
        bool: True if the user confirms deletion, False otherwise.
    """
    if not categories_to_delete:
        print("No categories meet the criteria for deletion.")
        return False

    print(f"This action will permanently delete {len(categories_to_delete)} categories with fewer than 3 posts.")
    user_input = input("Do you want to continue? Yes/No: ").strip().lower()
    return user_input in ['yes', 'y']

def display_final_confirmation(deleted_categories, errors):
    """
    Provides a summary to the user indicating the number of categories successfully deleted and any errors encountered.
    Args:
        deleted_categories (list): A list of categories that were successfully deleted.
        errors (list): A list of errors encountered during the deletion process.
    Returns:
        None
    """
    if deleted_categories:
        print(f"Successfully deleted {len(deleted_categories)} categories.")
        for category in deleted_categories:
            print(f"- {category}")
    else:
        print("No categories were deleted.")

    if errors:
        print("Errors encountered during deletion:")
        for error in errors:
            print(f"- {error}")
    else:
        print("No errors encountered during the deletion process.")

def log_information(deleted_categories, errors):
    """
    Optionally logs the information about deleted categories and errors for record-keeping.
    This function is a placeholder and should be implemented if logging is required.
    Args:
        deleted_categories (list): A list of categories that were successfully deleted.
        errors (list): A list of errors encountered during the deletion process.
    Returns:
        None
    """
    # This is a placeholder function. Implement logging as needed.
    pass
