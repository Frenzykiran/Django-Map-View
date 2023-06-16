# User Dashboard

User Dashboard is a web application built with Django that allows users to store and manage additional information such as username, city, location, project name, latitude, and longitude. The application provides a dashboard view to display the stored information in both a table/grid view and a map view.

## Features

- User registration and login functionality
- Additional info form to capture and store user data
- Dashboard view to display the stored data in a table/grid view and a map view
- Delete functionality to remove user data from the dashboard
- Toggle button to switch between the table/grid view and the map view

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Frenzykiran/Django-Map-View.git

2. Navigate to the project directory

3. Install the required dependencies using pip:
pip install -r requirements.txt

4. Set up the database:
python manage.py migrate

5. Create a superuser account:
python manage.py createsuperuser

6. "Make sure to replace YOUR_API_KEY in the dashboard.html template of the dashboardapp with your actual API key. If the script tag with the API key already exists, replace it with the following code:

<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY"></script>

7. Start the development server:
python manage.py runserver


