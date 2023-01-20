# Django Authentication Project

This is a Django project that demonstrates basic and social authentication functionality. It uses Django's built-in `User` model and the `social-auth-app-django` library to provide user authentication, including sign up, log in, log out, password reset, and social authentication via GitHub.

## Installation

1. Make sure Python 3.8+ and pip (Python package manager) are installed on your system.
2. Clone the repository:

    ```bash
    git clone https://github.com/thewolfcommander/django-api__authentication-system.git
    ```

3. Navigate to the project directory:

    ```bash
    cd django-authentication-project
    ```

4. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

5. Activate the virtual environment:

    On Windows, use:

    ```bash
    venv\Scripts\activate
    ```

    On Unix or MacOS, use:

    ```bash
    source venv/bin/activate
    ```

6. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

7. Apply the migrations:

    ```bash
    python manage.py migrate
    ```

8. Run the server:

    ```bash
    python manage.py runserver
    ```

The application will be available at http://localhost:8000.

## Features

- User Registration
- User Login
- User Logout
- Password Reset
- Profile Completion
- GitHub Authentication

## Configuration

This project uses GitHub for social authentication. You need to create a GitHub OAuth app and add the `Client ID` and `Client Secret` to your settings. For more details, refer to the [GitHub OAuth documentation](https://docs.github.com/en/developers/apps/building-oauth-apps).

The email backend is configured to use Django's console email backend by default. For a production system, you should use a real email backend.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
