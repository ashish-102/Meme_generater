# Meme Generator Web App

## Introduction

Welcome to the Meme Generator Web App! This web application allows users to create custom memes using a collection of pre-existing templates or by uploading their own images. It is built using Django, Python, HTML Canvas, CSS, JavaScript, and SQLite as the database.

## Features

- Upload your own images to create memes.
- Customize text and add coloe for your memes.
- Save and share your created memes.

## Installation

1. Clone this repository to your local machine.
   ```
   git clone https://github.com/ashish-102/meme-generator-web-app.git
   ```

2. Navigate to the project directory.
   ```
   cd Meme_generater
   ```

3. Install the required dependencies.
   ```
   pip install -r requirements.txt
   ```

4. Set up the database.
   ```
   python manage.py migrate
   ```

5. Run the development server.
   ```
   python manage.py runserver
   ```

6. Visit `http://localhost:8000` in your web browser to access the Meme Generator Web App.

## Usage

1. **Home Page**: The home page displays a list of available meme templates and options to upload your own image.

2. **Create Meme**: Select a meme template or upload your own image. Use the HTML canvas, CSS, and JavaScript functionality to add text and customize the appearance of your meme.

3. **Save Meme**: Once you are satisfied with your meme, click the "Save" button to store it in the SQLite database.

4. **View Memes**: Navigate to the "My Memes" page to view all the memes you have created.

## Technologies Used

- Django: A powerful web framework for Python that handles routing, database interactions, and more.
- Python: The programming language used to develop the backend logic.
- HTML Canvas: Used for rendering and customizing memes in the browser.
- CSS: Responsible for styling the user interface and layout.
- JavaScript: Provides interactivity and dynamic functionality to the web app.
- SQLite: A lightweight and easy-to-use database for storing meme data.

## Contribution

If you wish to contribute to this project, you are welcome to submit pull requests. Please follow the guidelines provided in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

Happy Meme Creating! 🎉
