from auth import get_app_token, test_authentication
from category_analysis import delete_categories

def main():
    try:
        # Step 1: Authentication
        print("Welcome to the Micro.blog Category Cleanup Tool.")
        app_token = get_app_token()
        test_authentication(app_token)
        print("Authentication successful.\n")

        # Step 5: Deleting Categories
        delete_categories(app_token)

        print("Category cleanup process completed.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()