# Simple Django Anime API  

A simple API built using Python and Django to learn Django. This API provides JSON data of anime, allowing users to view anime details, descriptions, and images. Users can also add anime to their "Watching" or "Plan to Watch" lists.  

## Table of Contents  
- [Overview](#overview)  
- [API Endpoints](#api-endpoints)  
- [Technologies Used](#technologies-used)  
- [Installation and Usage](#installation-and-usage)  
- [Skills Demonstrated](#skills-demonstrated)  
- [Database Design](#database-design)  

## Overview  
This project is a beginner-friendly Django application designed to explore the Django framework and REST API development. It includes basic user authentication and a simple SQLite database.  

## API Endpoints  
1. **Login**: Authenticate users.  
2. **Signup**: Register new users.  
3. **Home**: Display all anime in the database.  
4. **Anime**: Show detailed information about a specific anime.  
5. **Test**: For testing and development purposes.  

## Technologies Used  
- Python  
- Django  
- Django REST Framework  
- Basic User Authentication  
- SQLite Database  
- HTML Templates  

## Installation and Usage  
1. Clone the repository:  
    ```bash  
    git clone <repository-url>  
    ```  
2. Create virtual environment (optional but recommended):  
    ```bash  
    python -m venv venv  
    ```
3. Activate the virtual environment:  
    - On Windows:  
      ```bash  
      venv\Scripts\activate  
      ```  
    - On macOS/Linux:  
      ```bash  
      source venv/bin/activate  
      ```
4. Navigate to the project directory:  
    ```bash  
    cd Simple-DjangoApp  
    ```  
5. Install dependencies:  
    ```bash  
    pip install -r requirements.txt  
    ```  
6. Run migrations:  
    ```bash  
    python manage.py migrate  
    ```  
7. Start the development server:  
    ```bash  
    python manage.py runserver  
    ```  
8. Access the app at `http://127.0.0.1:8000/`.  

## Skills Demonstrated  
- Building RESTful APIs with Django REST Framework.  
- Implementing user authentication.  
- Designing and managing a relational database.  
- Using Django templates for HTML rendering.  

## Database Design  
Below is a simple representation of the database structure:  

![Database Design](https://via.placeholder.com/600x400?text=Database+Design+Diagram)  

- **Anime Table**: Stores anime details (name, description, image URL).  
- **User Table**: Stores user information.  
- **UserAnime Table**: Tracks user-specific anime lists (Watching, Plan to Watch).  

---  
Enjoy exploring the world of Django and building APIs!  