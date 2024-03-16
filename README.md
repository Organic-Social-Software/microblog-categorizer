# Micro.blog Category Cleaner

This Python script is designed to interact with the micro.blog platform to batch edit blog categories. Specifically, it deletes categories with fewer than 3 posts associated with them, adhering to the Micropub API standards for managing post metadata and using app tokens for authentication.

## Getting Started

### Prerequisites

- Python 3.x
- A micro.blog account and an app token

### Installation

1. Clone this repository or download the source code.
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Obtain your micro.blog app token from your micro.blog account under Account → Edit Apps.

### Configuration

For security reasons, it's recommended to store your micro.blog app token in an environment variable or a secure vault. The script prompts you to enter the token when it runs, ensuring your token is not hard-coded.

## Usage

Run the script from the command line:

```bash
python main.py
```

Follow the on-screen instructions to authenticate and proceed with the category deletion process.

### Steps Performed by the Script

1. **Authentication**: The script starts by accepting your micro.blog app token and uses it to authenticate API requests.
2. **Fetching Posts and Categories**: It then fetches all posts from your micro.blog and aggregates category information.
3. **Identifying Categories to Delete**: The script identifies categories with fewer than 3 posts and presents them to you for review.
4. **Confirmation Steps**: You're prompted for confirmation before proceeding with the deletion of the identified categories.
5. **Deleting Categories**: Upon confirmation, the script updates each post's metadata to remove the category since direct deletion of categories is not supported.
6. **Final Confirmation**: After the deletion process, a summary is provided, indicating the number of categories successfully deleted and any errors encountered.

## Files

- `auth.py`: Handles authentication, including token retrieval and validation.
- `api_communication.py`: Manages API communication, including fetching posts and updating post categories.
- `data_processing.py`: Processes data, including aggregating categories and identifying categories to delete.
- `user_interaction.py`: Manages user interaction, including confirmation prompts and displaying summaries.
- `main.py`: The main script that orchestrates the workflow.
- `requirements.txt`: Lists the Python package dependencies.
- `README.md`: This file, providing an overview and instructions.

## Security and Best Practices

- Never hard-code your app token within the script.
- Store your token in an environment variable or a secure vault accessible by the script.

## Documentation and Comments

The script includes detailed comments explaining each step and API request for clarity and maintainability.

## License

This project is open-source and available under the MIT License.

