# News Forum

## Introduction & Overview

News Forum is a web application built with Django, designed for users to create, read, update, and delete posts, as well as to comment on posts. The project demonstrates the application of Python programming concepts and Django’s Model-View-Template (MVT) architecture. The platform is suitable for users who enjoy sharing and discussing news topics in a community setting.

You can view the live application [here](https://news-forum-e420302f60a9.herokuapp.com/).

## Features

This implementation includes features such as:

- User authentication: Registration, login, and logout functionality.
- CRUD operations for posts and comments: Users can create, read, edit, and delete posts and comments.
- Category management: Each post can be associated with a category.
- User-friendly interface with responsive design.
- Security features: Only authenticated users can create or comment on posts.

### Screenshots

![Home Page](screenshots/homepage.png)

![Post Detail Page](screenshots/post_detail.png)

![Login Page](screenshots/login.png)

## Project Rationale and Design Decisions

### Security Enhancements

To enhance the security of the News Forum application, several measures were implemented:

- **Environment Variables:** Sensitive information such as the `SECRET_KEY` and email credentials are stored in environment variables using a `.env` file. This ensures that these details are not exposed in the code repository.
- **Secure Cookies:** The application uses secure settings for cookies (`SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`) to prevent security vulnerabilities like Cross-Site Request Forgery (CSRF).
- **HTTPS Redirect:** The application forces HTTPS connections with `SECURE_SSL_REDIRECT` to ensure secure communication between the client and the server.

### Object-Oriented Programming and Django Framework

The project leverages Django’s MVT architecture, which organizes the code into distinct components for models, views, and templates, promoting a clean and maintainable codebase. 

- **Models:** Define the data structure of the application, such as `Post` and `Comment`, and are linked with Django’s ORM for database interactions.
- **Views:** Handle the logic for rendering templates and processing data. For example, the `post_detail` view retrieves and displays post details.
- **Templates:** Use Django's template language to render HTML pages dynamically based on the data passed by views.

Some of the key methods and components include:

- **Model Inheritance:** Extending Django’s `Model` class to define the data schema.
- **Form Handling:** Utilizing Django’s `ModelForm` to manage form input and validation.
- **Authentication Decorators:** Protecting views with `@login_required` to ensure that only authenticated users can perform certain actions.

## Development Process

### Agile Methodology and User Stories

The development of the News Forum application followed an Agile methodology, focusing on iterative development and continuous feedback. Key functionalities were planned and tracked using user stories. For example:

- **User Story 1:** "As a registered user, I want to create a new post so that I can share information with other users."
- **User Story 2:** "As a registered user, I want to delete my account so that I can remove my presence from the platform."

These user stories were documented and implemented using GitHub's Issues feature, allowing for efficient tracking and progress monitoring throughout the project lifecycle.

## Testing

### Unit Testing

Unit tests were created to verify the functionality of models, views, and forms. These tests ensure the application behaves as expected under various scenarios. For example, the `PostModelTest` checks that posts are correctly created and associated with categories, while `CommentModelTest` verifies comment functionality.

You can run the unit tests by executing:

```bash
python manage.py test

### Manual Testing

In addition to unit testing, manual testing was conducted to validate the user experience, such as ensuring that forms display appropriate error messages and restricted actions (like post creation) are only available to logged-in users.

- **User Authentication:** Tested the signup, login, and logout functionalities with valid and invalid credentials.
- **Post Management:** Created, edited, and deleted posts to ensure the correctness of the operations.
- **Comment System:** Verified that comments could be added, edited, and deleted, and that only the comment owner could perform these actions.

### Bugs

- **Comment Submission Issue:** A bug was encountered where submitting a comment while logged out resulted in an error. This was resolved by redirecting unauthenticated users to the login page.

### Password Reset Functionality

This project includes a password reset feature that allows users to reset their passwords in case they forget them. The functionality is implemented using Django's built-in authentication views, which handle the password reset process through email verification.

#### Steps for Password Reset:

1. Users can initiate the password reset process by clicking on the "Forgot your password?" link on the login page.
2. The user will be prompted to enter their registered email address.
3. If the email address is associated with an account, a password reset link will be sent to that email.
4. The user can follow the link in the email to reset their password.

#### Current Status:

- **Bug:** The password reset functionality is not fully operational due to issues with SMTP authentication when attempting to send the reset email. Specifically, the application is encountering an `SMTPAuthenticationError` related to Google’s security settings.
  
- **Resolution:** The issue is likely due to missing or incorrect configuration of an app-specific password in the email service used for sending the reset emails. Once the app-specific password is correctly set up, the feature should work as intended.

### Tools and Resources

- [Django](https://www.djangoproject.com/): The main web framework used to build the application.
- [Python](https://www.python.org/): The programming language used for the backend logic.
- [PostgreSQL](https://www.postgresql.org/): The database used in both development and production environments.
- [Git](https://git-scm.com/): For version control.
- [GitHub](https://github.com/): Hosting the code repository.
- [Heroku](https://www.heroku.com/): Platform for deploying the live application.

## Deployment

### Heroku

The News Forum application is deployed on Heroku. To deploy your own version:

1. **Create a New Heroku App**: Use the Heroku dashboard or CLI to create a new app.
2. **Set Up Buildpacks**: Configure the buildpacks for Python in your Heroku app settings.
3. **Link to GitHub**: Connect your Heroku app to your GitHub repository for automatic deployment.
4. **Deploy the Application**: Deploy manually or set up automatic deploys from the GitHub branch.

```bash
# Environment Configuration

# To ensure the application runs securely and efficiently on Heroku, 
# several environment variables need to be configured. 
# These are essential for settings like email functionality and security:

# SECRET_KEY: A unique, unpredictable value used for cryptographic signing. 
# This should be set as an environment variable on Heroku to keep it secure.
heroku config:set SECRET_KEY=your-secret-key

# EMAIL_HOST_USER: The email address used to send emails from the application, 
# such as password reset emails.
heroku config:set EMAIL_HOST_USER=your-email@example.com

# EMAIL_HOST_PASSWORD: The password for the email account. 
# If using Gmail, ensure that you use an App Password if two-factor authentication is enabled.
heroku config:set EMAIL_HOST_PASSWORD=your-email-password

# DEBUG: Ensure that DEBUG is set to False in production to avoid exposing sensitive information.
heroku config:set DEBUG=False

# Additional Security Settings
# For enhanced security in a production environment, the following settings have been configured:

1. SSL Redirection: All traffic is redirected to HTTPS to ensure data is encrypted in transit.

2. HTTP Strict Transport Security (HSTS): Enforces secure connections to the server.

3. Secure Cookies: Cookies like SESSION_COOKIE and CSRF_COOKIE are marked as secure
to ensure they are only sent over HTTPS.

4. Content Security: Prevents the application from loading content 
that may introduce vulnerabilities, such as cross-site scripting (XSS).

# Deployment Process

# After setting the necessary environment variables, follow these steps to complete the deployment:

# Collect Static Files: Run the following command to gather static files before deployment:
heroku run python manage.py collectstatic --noinput

# Run Migrations: Apply any database migrations required by your Django models:
heroku run python manage.py migrate

# Restart the Application: Ensure that all changes are applied by restarting the Heroku dynos:
heroku restart

## Local Development Setup

### Prerequisites

- Python 3.6 or later
- Git for version control

### Setting Up the Environment

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/darvid-223/news-forum.git
    cd news-forum
    ```

2. **Create a `.env` file for storing secret keys and credentials**:
    ```bash
    touch .env
    ```

3. **Create and Activate a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Apply Migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

Make sure to populate the `.env` file with the necessary environment variables such as `SECRET_KEY`, `DB_PASSWORD`, `EMAIL_HOST_USER`, and `EMAIL_HOST_PASSWORD`.

## Credits & Acknowledgments

### Acknowledgements

- Special thanks to my friend Lucas Behrendt, whose feedback and tips from his experience in the same course were immensely helpful.
- Special thanks to [Udemy's 100 Days of Code: The Complete Python Pro Bootcamp for 2023](https://www.udemy.com/course/100-days-of-code/) for providing comprehensive lessons on Python and object-oriented programming, which significantly contributed to the development of this project.
- **Fictional Articles**: ChatGPT was used to generate fictional news articles used as sample posts for demonstrating the application's functionality.

This project was developed with the assistance of OpenAI's ChatGPT in the following areas:
- **Code Validation**: ChatGPT helped validate the syntax and logic of the code.
- **Spelling and Grammar Checks**: Assisted in checking and correcting spelling and grammar in the documentation and code comments.
- **Translations**: Provided translations for multilingual support in the documentation.
- **Coding Advice**: Offered suggestions and advice on coding practices and problem-solving approaches.
- **Content Generation**: Assisted in generating fictional content for the posts displayed on the site.
- **Real-Time Troubleshooting**: Supported real-time debugging and troubleshooting during the development process.

Special thanks to [OpenAI's ChatGPT](https://openai.com/) for its invaluable support in refining the content and functionality of this project.
