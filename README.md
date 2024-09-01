# News Forum

## Introduction & Overview

News Forum is a web application built with Django, designed for users to create, read, update, and delete posts, as well as to comment on posts. The project demonstrates the application of Python programming concepts and Django’s Model-View-Template (MVT) architecture. The platform is suitable for users who enjoy sharing and discussing news topics in a community setting.

You can view the live application [here]( >LÄgg IN LÄNK).

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

### Object-Oriented Programming and Django Framework

The project leverages Django’s MVT architecture, which organizes the code into distinct components for models, views, and templates, promoting a clean and maintainable codebase. 

- **Models:** Define the data structure of the application, such as `Post` and `Comment`, and are linked with Django’s ORM for database interactions.
- **Views:** Handle the logic for rendering templates and processing data. For example, the `post_detail` view retrieves and displays post details.
- **Templates:** Use Django's template language to render HTML pages dynamically based on the data passed by views.

Some of the key methods and components include:

- **Model Inheritance:** Extending Django’s `Model` class to define the data schema.
- **Form Handling:** Utilizing Django’s `ModelForm` to manage form input and validation.
- **Authentication Decorators:** Protecting views with `@login_required` to ensure that only authenticated users can perform certain actions.

## Testing

### Unit Testing

Unit tests were created to verify the functionality of the models and views, ensuring that the application behaves as expected. These tests help in identifying and fixing bugs early in the development process.

### Manual Testing

In addition to unit testing, manual testing was conducted to validate the user experience and application flow:

- **User Authentication:** Tested the signup, login, and logout functionalities with valid and invalid credentials.
- **Post Management:** Created, edited, and deleted posts to ensure the correctness of the operations.
- **Comment System:** Verified that comments could be added, edited, and deleted, and that only the comment owner could perform these actions.

### Bugs

- **Comment Submission Issue:** A bug was encountered where submitting a comment while logged out resulted in an error. This was resolved by redirecting unauthenticated users to the login page.

### Tools and Resources

- [Django](https://www.djangoproject.com/): The main web framework used to build the application.
- [Python](https://www.python.org/): The programming language used for the backend logic.

    LÄGG IN SQL
- [SQLite](https://www.sqlite.org/index.html): Used as the database during development.


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

## Local Development Setup

### Introduction

For local development, this project is set up to run on a Python virtual environment. Visual Studio Code is recommended for its powerful features and integration with Git.

### Prerequisites

- Python 3.6 or later
- Git for version control

### Setting Up the Environment

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/news-forum.git
    cd news-forum
    ```

2. **Create and Activate a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

## Credits & Acknowledgments

### Acknowledgements

- Special thanks to my friend Lucas Behrendt, whose feedback and tips from his experience in the same course were immensely helpful.

- Special thanks to [Udemy's 100 Days of Code: The Complete Python Pro Bootcamp for 2023](https://www.udemy.com/course/100-days-of-code/) for providing comprehensive lessons on Python and object-oriented programming, which significantly contributed to the development of this project.

This project was developed with the assistance of OpenAI's ChatGPT in the following areas:
- **Code Validation**: ChatGPT helped validate the syntax and logic of the code.
- **Spelling and Grammar Checks**: Assisted in checking and correcting spelling and grammar in the documentation and code comments.
- **Translations**: Provided translations for multilingual support in the documentation.
- **Coding Advice**: Offered suggestions and advice on coding practices and problem-solving approaches.
- **Content Generation**: Assisted in generating content for the README and other documentation.
- **Real-Time Troubleshooting**: Supported real-time debugging and troubleshooting during the development process.

Special thanks to [OpenAI's ChatGPT](https://openai.com/) for its invaluable support in refining the content and functionality of this project.